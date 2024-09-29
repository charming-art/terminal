import path from "path";
import {defineConfig} from "vite";

export default defineConfig({
  root: path.resolve("./test"),
  server: {
    port: 8080,
    open: "/",
  },
  resolve: {
    alias: {
      "@charming-art/cell": path.resolve("./src/index.js"),
      "../wasm/index_bg.wasm": "../wasm/index_bg.wasm?url",
    },
  },
  build: {outDir: "../"},
});
