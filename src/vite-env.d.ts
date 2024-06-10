/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_TRUESHUFFLE_AI_API_URL?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}

