import node from "@rollup/plugin-node-resolve";
import { wasm } from "@rollup/plugin-wasm";
import terser from "@rollup/plugin-terser";

const config = {
  input: "src/index.js",
  output: {
    format: "umd",
    name: "cm",
  },
  plugins: [wasm({ targetEnv: "auto-inline" }), node()],
};

export default [
  {
    ...config,
    output: {
      ...config.output,
      file: "dist/cm.umd.js",
    },
  },
  {
    ...config,
    output: {
      ...config.output,
      file: "dist/cm.umd.min.js",
    },
    plugins: [...config.plugins, terser()],
  },
];
