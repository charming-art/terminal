import path from "path";
import { defineConfig } from "vite";

export default defineConfig({
  root: "./test",
  server: {
    port: 8080,
    open: "/",
  },
  resolve: {
    alias: {
      "@charming-art/charming": path.resolve("./src/index.js"),
      "@charming-art/charming-canvas": path.resolve("./src/canvas.js"),
    },
  },
});
