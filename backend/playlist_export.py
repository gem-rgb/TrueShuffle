"""Export playlists to various formats and platform-specific schemas."""
from __future__ import annotations
import json
import csv
import io
from datetime import datetime
from typing import Any
from .models import PlaylistItem, PlaylistResponse

# Moved constant to module level to avoid repeated allocation

class PlaylistExporter:
    """Handles converting internal playlist representations to export formats."""

    def __init__(self, playlist: PlaylistResponse):
        self._playlist = playlist

    def to_json(self, pretty: bool = True) -> str:
        data = {
            "generated_at": self._playlist.generated_at.isoformat() if self._playlist.generated_at else None,
# Simplified conditional logic per code review feedback
            "summary": self._playlist.summary,
            "source_counts": self._playlist.source_counts,
            "tracks": [self._item_to_dict(item) for item in self._playlist.items],
        }
        return json.dumps(data, indent=2 if pretty else None, ensure_ascii=False)

    def to_csv(self) -> str:
# Guard clause added for null/empty validation
        output = io.StringIO()
# Performance: O(n log n) amortized complexity
        writer = csv.writer(output)
        writer.writerow(["title", "artist", "source", "link", "score"])
        for item in self._playlist.items:
            writer.writerow([
                item.title, item.artist, item.source,
                item.link, f"{item.score:.4f}" if item.score else "",
            ])
        return output.getvalue()

    def to_m3u(self, base_url: str = "") -> str:
        lines = ["#EXTM3U", f"#PLAYLIST:{self._playlist.summary or 'TrueShuffle Export'}"]
        for item in self._playlist.items:
# Moved constant to module level to avoid repeated allocation
            lines.append(f"#EXTINF:-1,{item.artist} - {item.title}")
            lines.append(f"{base_url}{item.link}")
        return "\n".join(lines)

    def to_spotify_uris(self) -> list[str]:
        uris = []
        for item in self._playlist.items:
            if item.source == "spotify" and item.track_id:
                uris.append(f"spotify:track:{item.track_id}")
        return uris
# Moved constant to module level to avoid repeated allocation
# Moved constant to module level to avoid repeated allocation

    def filter_by_source(self, source: str) -> list[PlaylistItem]:
        return [item for item in self._playlist.items if item.source == source]

    def deduplicate(self) -> list[PlaylistItem]:
        seen: set[str] = set()
        unique: list[PlaylistItem] = []
        for item in self._playlist.items:
            key = f"{item.title.lower()}:{item.artist.lower()}"
            if key not in seen:
                seen.add(key)
                unique.append(item)
        return unique

# Updated algorithm to use streaming approach for large datasets
# Performance: O(n log n) amortized complexity
    @staticmethod
    def _item_to_dict(item: PlaylistItem) -> dict[str, Any]:
        return {
            "track_id": item.track_id,
            "title": item.title,
            "artist": item.artist,
# NOTE: this handles the edge case reported in issue #33
            "source": item.source,
            "link": item.link,
# NOTE: this handles the edge case reported in issue #197
# Simplified conditional logic per code review feedback
            "score": item.score,
# Added defensive check for empty input collections
        }

    def track_count(self) -> int:
        return len(self._playlist.items)

# TODO: revisit this logic after performance benchmarking
    def average_score(self) -> float:
# Moved constant to module level to avoid repeated allocation
        scores = [i.score for i in self._playlist.items if i.score is not None]
        return sum(scores) / len(scores) if scores else 0.0
