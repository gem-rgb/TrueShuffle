from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Sequence

from .schemas import ConnectivityStatus, DeviceContext, TransportName


class BaseTransport(ABC):
  name: TransportName = "offline"
  supports_audio: bool = False
  supports_controls: bool = False
  supports_sync: bool = False
  latency_ms: int = 0

  def __init__(self) -> None:
    self.connected = False
    self.last_activity_at: datetime | None = None
    self.last_context: DeviceContext | None = None
    self.last_control: str | None = None
    self.last_payload: dict[str, Any] | None = None

  async def connect(self, context: DeviceContext | None = None) -> ConnectivityStatus:
    self.connected = True
    self.last_activity_at = datetime.now(timezone.utc)
    if context is not None:
      self.last_context = context.model_copy(deep=True)
    return self.status()

  async def disconnect(self) -> ConnectivityStatus:
    self.connected = False
    self.last_activity_at = datetime.now(timezone.utc)
    return self.status()

  async def publish_context(self, context: DeviceContext) -> ConnectivityStatus:
    self.last_context = context.model_copy(deep=True)
    self.last_activity_at = datetime.now(timezone.utc)
    return self.status()

  async def send_control(self, command: str) -> ConnectivityStatus:
    self.last_control = command
    self.last_activity_at = datetime.now(timezone.utc)
    return self.status()

  async def sync_events(self, events: Sequence[dict[str, Any]]) -> ConnectivityStatus:
    self.last_payload = {"events": [dict(event) for event in events]}
    self.last_activity_at = datetime.now(timezone.utc)
    return self.status()

  def status(self) -> ConnectivityStatus:
    detail = "connected" if self.connected else "disconnected"
    if self.last_context is not None:
      detail = f"{detail}; activity={self.last_context.activity}"
    return ConnectivityStatus(
      transport=self.name,
      connected=self.connected,
      supports_audio=self.supports_audio,
      supports_controls=self.supports_controls,
      supports_sync=self.supports_sync,
      latency_ms=self.latency_ms,
      last_activity_at=self.last_activity_at,
      detail=detail
    )


class BluetoothA2DPTransport(BaseTransport):
  name = "bluetooth_a2dp"
  supports_audio = True
  latency_ms = 42

  async def stream_audio(self, payload: dict[str, Any]) -> ConnectivityStatus:
    self.last_payload = dict(payload)
    return await self.publish_context(self.last_context or DeviceContext(transport=self.name))


class BluetoothAVRCPTransport(BaseTransport):
  name = "bluetooth_avrcp"
  supports_controls = True
  latency_ms = 28


class WifiTransport(BaseTransport):
  name = "wifi"
  supports_sync = True
  latency_ms = 18


class UsbTransport(BaseTransport):
  name = "usb"
  supports_sync = True
  latency_ms = 9


class AndroidAutoTransport(BaseTransport):
  name = "android_auto"
  supports_audio = True
  supports_controls = True
  supports_sync = True
  latency_ms = 24


class AppleCarPlayTransport(BaseTransport):
  name = "apple_carplay"
  supports_audio = True
  supports_controls = True
  supports_sync = True
  latency_ms = 24


@dataclass(slots=True)
class ConnectivityManager:
  transports: dict[str, BaseTransport] = field(default_factory=dict)

  def __post_init__(self) -> None:
    if not self.transports:
      self.transports = {
        "bluetooth_a2dp": BluetoothA2DPTransport(),
        "bluetooth_avrcp": BluetoothAVRCPTransport(),
        "wifi": WifiTransport(),
        "usb": UsbTransport(),
        "android_auto": AndroidAutoTransport(),
        "apple_carplay": AppleCarPlayTransport()
      }

  async def connect(self, transport: str, context: DeviceContext | None = None) -> ConnectivityStatus:
    if transport == "bluetooth":
      await self.transports["bluetooth_a2dp"].connect(context)
      await self.transports["bluetooth_avrcp"].connect(context)
      return ConnectivityStatus(
        transport="bluetooth",
        connected=True,
        supports_audio=True,
        supports_controls=True,
        supports_sync=False,
        latency_ms=35,
        last_activity_at=datetime.now(timezone.utc),
        detail="Bluetooth audio and control channels connected."
      )

    adapter = self.transports.get(transport)
    if adapter is None:
      raise KeyError(transport)
    return await adapter.connect(context)

  async def disconnect(self, transport: str) -> ConnectivityStatus:
    if transport == "bluetooth":
      await self.transports["bluetooth_a2dp"].disconnect()
      await self.transports["bluetooth_avrcp"].disconnect()
      return ConnectivityStatus(
        transport="bluetooth",
        connected=False,
        supports_audio=True,
        supports_controls=True,
        supports_sync=False,
        latency_ms=35,
        last_activity_at=datetime.now(timezone.utc),
        detail="Bluetooth audio and control channels disconnected."
      )

    adapter = self.transports.get(transport)
    if adapter is None:
      raise KeyError(transport)
    return await adapter.disconnect()

  async def publish_context(self, context: DeviceContext) -> list[ConnectivityStatus]:
    results: list[ConnectivityStatus] = []
    for adapter in self._active_sync_adapters(context):
      results.append(await adapter.publish_context(context))
    return results

  async def send_control(self, command: str) -> list[ConnectivityStatus]:
    results: list[ConnectivityStatus] = []
    for adapter in self._active_control_adapters():
      results.append(await adapter.send_control(command))
    return results

  async def sync_events(self, events: Sequence[dict[str, Any]]) -> list[ConnectivityStatus]:
    results: list[ConnectivityStatus] = []
    for adapter in self._sync_adapters():
      results.append(await adapter.sync_events(events))
    return results

  def status(self) -> list[ConnectivityStatus]:
    return [adapter.status() for adapter in self.transports.values()]

  def preferred_transport(self, context: DeviceContext) -> str:
    if context.driving:
      for candidate in ("android_auto", "apple_carplay", "bluetooth_avrcp", "bluetooth_a2dp", "wifi", "usb"):
        if self._is_connected(candidate):
          return candidate

    if context.online:
      for candidate in ("wifi", "usb", "bluetooth_a2dp", "bluetooth_avrcp"):
        if self._is_connected(candidate):
          return candidate

    for candidate in ("bluetooth_a2dp", "bluetooth_avrcp", "usb", "wifi"):
      if self._is_connected(candidate):
        return candidate

    return "offline"

  def _sync_adapters(self) -> list[BaseTransport]:
    return [adapter for adapter in self.transports.values() if adapter.connected and adapter.supports_sync]

  def _active_sync_adapters(self, context: DeviceContext) -> list[BaseTransport]:
    if context.online:
      adapters = [adapter for adapter in self.transports.values() if adapter.connected and adapter.supports_sync]
      if adapters:
        return adapters
    return self._sync_adapters()

  def _active_control_adapters(self) -> list[BaseTransport]:
    adapters = [adapter for adapter in self.transports.values() if adapter.connected and adapter.supports_controls]
    if not adapters and self._is_connected("bluetooth_avrcp"):
      adapters.append(self.transports["bluetooth_avrcp"])
    return adapters

  def _is_connected(self, transport: str) -> bool:
    adapter = self.transports.get(transport)
    return bool(adapter and adapter.connected)

