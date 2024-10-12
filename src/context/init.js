import {Terminal} from "../terminal.js";
import {Renderer} from "../wasm/index.js";
import init from "../wasm/index.js";
import wasm from "../wasm/index_bg.wasm";

export async function context_init(options = {}) {
  const module = await init(typeof wasm === "function" ? await wasm() : undefined);
  const {memory} = module;
  const terminal = new Terminal(options);
  const renderer = Renderer.new(terminal._cols, terminal._rows);
  this._memory = memory;
  this._terminal = terminal;
  this._renderer = renderer;
  this._terminal.background("#000");
  return this;
}
