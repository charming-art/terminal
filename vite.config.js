import path from "path";
import { defineConfig } from "vite";

export default defineConfig({
  root: path.resolve("./test"),
  server: {
    port: 8080,
    open: "/",
  },
  resolve: {
    alias: {
      "@charming-art/charming": path.resolve("./src/index.js"),
      "@charming-art/charming-canvas": path.resolve("./src/canvas.js"),
      "./wasm/index_bg.wasm": "./wasm/index_bg.wasm?url",
    },
  },
  test: { globalSetup: path.resolve("./server.js") },
  build: { outDir: "../" },
});
