import node from "@rollup/plugin-node-resolve";
import {wasm} from "@rollup/plugin-wasm";
import terser from "@rollup/plugin-terser";

const umd = {
  input: "src/index.js",
  output: {
    format: "umd",
    name: "Cell",
  },
  plugins: [wasm({targetEnv: "auto-inline"}), node()],
};

export default [
  {
    input: "src/index.js",
    output: {
      format: "es",
      dir: "dist/es",
      preserveModules: true,
    },
    external: [/node_modules/],
    plugins: [wasm({targetEnv: "auto-inline"}), node()],
  },
  {
    ...umd,
    output: {
      ...umd.output,
      file: "dist/cell.umd.js",
    },
  },
  {
    ...umd,
    output: {
      ...umd.output,
      file: "dist/cell.umd.min.js",
    },
    plugins: [...umd.plugins, terser()],
  },
];
