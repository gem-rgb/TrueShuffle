import { createReadStream, existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import http from "node:http";
import path from "node:path";
import { spawn, spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const rootDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const distDir = path.join(rootDir, "dist");
const srcEntry = path.join(rootDir, "src", "main.tsx");
const indexHtmlPath = path.join(rootDir, "index.html");
const windowsEsbuildBinary = path.join(rootDir, "node_modules", "@esbuild", "win32-x64", "esbuild.exe");

const entryArgs = [
  srcEntry,
  "--bundle",
  "--outdir=dist/assets",
  "--entry-names=index",
  "--format=esm",
  "--platform=browser",
  "--target=es2020",
  "--sourcemap",
  "--jsx=automatic",
  "--jsx-import-source=react",
  "--loader:.css=css"
];

function ensureDistHtml() {
  const html = readFileSync(indexHtmlPath, "utf8");
  const rewritten = html.replace(
    '<script type="module" src="/src/main.tsx"></script>',
    '<link rel="stylesheet" href="/assets/index.css" />\n    <script type="module" src="/assets/index.js"></script>'
  );
  mkdirSync(distDir, { recursive: true });
  writeFileSync(path.join(distDir, "index.html"), rewritten, "utf8");
}

function runCommand(command, args, options = {}) {
  const result = spawnSync(command, args, {
    cwd: rootDir,
    stdio: "inherit",
    shell: false,
    ...options
  });

  if (result.error) {
    throw result.error;
  }
  if (result.status !== 0) {
    throw new Error(`${command} exited with code ${result.status ?? "unknown"}`);
  }
}

function runWindowsBuild() {
  rmSync(distDir, { recursive: true, force: true });
  mkdirSync(path.join(distDir, "assets"), { recursive: true });
  runCommand(windowsEsbuildBinary, entryArgs);
  ensureDistHtml();
}

function runWindowsDev() {
  rmSync(distDir, { recursive: true, force: true });
  mkdirSync(path.join(distDir, "assets"), { recursive: true });
  ensureDistHtml();

  runCommand(windowsEsbuildBinary, entryArgs);

  const watchProcess = spawn(windowsEsbuildBinary, [...entryArgs, "--watch=forever"], {
    cwd: rootDir,
    stdio: "inherit",
    shell: false
  });

  watchProcess.on("exit", (code) => {
    const exitCode = code ?? 0;
    if (exitCode !== 0) {
      console.error(`esbuild watch exited with code ${exitCode}`);
    }
    process.exit(exitCode);
  });

  const server = serveDist();
  const shutdown = () => {
    watchProcess.kill();
    server.close(() => process.exit(0));
  };

  process.on("SIGINT", shutdown);
  process.on("SIGTERM", shutdown);
}

function serveDist(port = 1420, host = "127.0.0.1") {
  const server = http.createServer((req, res) => {
    const requestUrl = new URL(req.url ?? "/", `http://${host}:${port}`);
    const normalizedPath = requestUrl.pathname === "/" ? "/index.html" : requestUrl.pathname;
    const candidatePath = path.normalize(path.join(distDir, decodeURIComponent(normalizedPath)));
    const safeRoot = distDir.endsWith(path.sep) ? distDir : `${distDir}${path.sep}`;

    if (!candidatePath.startsWith(safeRoot) && candidatePath !== path.join(distDir, "index.html")) {
      res.writeHead(403);
      res.end("Forbidden");
      return;
    }

    const filePath = existsSync(candidatePath) ? candidatePath : path.join(distDir, "index.html");
    const ext = path.extname(filePath).toLowerCase();
    const contentType = {
      ".css": "text/css; charset=utf-8",
      ".html": "text/html; charset=utf-8",
      ".ico": "image/x-icon",
      ".js": "text/javascript; charset=utf-8",
      ".json": "application/json; charset=utf-8",
      ".map": "application/json; charset=utf-8",
      ".png": "image/png",
      ".svg": "image/svg+xml",
      ".txt": "text/plain; charset=utf-8"
    }[ext] ?? "application/octet-stream";

    res.writeHead(200, {
      "Content-Type": contentType,
      "Cache-Control": "no-store"
    });
    createReadStream(filePath).pipe(res);
  });

  server.on("error", (error) => {
    if (error && typeof error === "object" && error.code === "EADDRINUSE") {
      setTimeout(() => {
        server.close(() => {
          server.listen(port, host);
        });
      }, 500);
      return;
    }
    console.error(error);
    process.exit(1);
  });

  server.listen(port, host, () => {
    console.log(`TrueShuffle dev server running at http://${host}:${port}`);
  });

  return server;
}

function runNonWindowsBuild() {
  runCommand("npm", ["exec", "vite", "build"]);
}

function runNonWindowsDev() {
  runCommand("npm", ["exec", "vite"]);
}

const mode = process.argv[2];

if (mode === "build") {
  if (process.platform === "win32") {
    runWindowsBuild();
  } else {
    runNonWindowsBuild();
  }
} else if (mode === "dev") {
  if (process.platform === "win32") {
    runWindowsDev();
    serveDist();
  } else {
    runNonWindowsDev();
  }
} else {
  console.error("Usage: node scripts/frontend.mjs <build|dev>");
  process.exit(1);
}
