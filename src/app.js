import init from "./wasm/index.js";
import wasm from "./wasm/index_bg.wasm";
import { App } from "./app/index.js";

export async function app(options) {
  const module = await init(typeof wasm === "function" ? await wasm() : undefined);
  const { memory } = module;
  return new App(memory, options);
}
