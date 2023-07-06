import node from "@rollup/plugin-node-resolve";
import { wasm } from "@rollup/plugin-wasm";
import terser from "@rollup/plugin-terser";

const umd = {
  input: "src/index.js",
  output: {
    format: "umd",
    name: "cm",
  },
  plugins: [wasm({ targetEnv: "auto-inline" }), node()],
};

export default [
  {
    input: "src/index.js",
    output: {
      format: "es",
      dir: "dist/es",
      preserveModules: true,
    },
    plugins: [wasm()],
  },
  {
    ...umd,
    output: {
      ...umd.output,
      file: "dist/cm.umd.js",
    },
  },
  {
    ...umd,
    output: {
      ...umd.output,
      file: "dist/cm.umd.min.js",
    },
    plugins: [...umd.plugins, terser()],
  },
];
