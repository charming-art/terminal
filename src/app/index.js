import { Terminal } from "../terminal.js";
import { Renderer } from "../wasm/index.js";
import { app$render } from "./render.js";
import { app$scene, app$stroke } from "./attributes.js";
import { app$point } from "./primitives.js";
import { app$cols, app$rows, app$node } from "./variables.js";

export function App({ memory, ...options } = {}) {
  const terminal = new Terminal(options);
  const cols = terminal.cols();
  const rows = terminal.rows();
  const renderer = Renderer.new(cols, rows);
  Object.defineProperties(this, {
    _memory: { value: memory },
    _terminal: { value: terminal },
    _renderer: { value: renderer },
    _cols: { value: cols },
    _rows: { value: rows },
    _fill: { value: "#000000", writable: true },
  });
}

Object.defineProperties(App.prototype, {
  render: { value: app$render, writable: true, configurable: true },
  stroke: { value: app$stroke, writable: true, configurable: true },
  scene: { value: app$scene, writable: true, configurable: true },
  point: { value: app$point, writable: true, configurable: true },
  cols: { value: app$cols, writable: true, configurable: true },
  rows: { value: app$rows, writable: true, configurable: true },
  node: { value: app$node, writable: true, configurable: true },
});
