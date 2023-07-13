import { Terminal } from "../terminal.js";
import { Renderer } from "../wasm/index.js";
import { app$render } from "./render.js";
import { app$scene, app$stroke } from "./attributes.js";
import { app$point } from "./primitives.js";
import {
  app$cols,
  app$rows,
  app$node,
  app$fontFamily,
  app$fontSize,
  app$fontWeight,
  app$height,
  app$width,
  app$cellHeight,
  app$cellWidth,
} from "./variables.js";

export function App({ memory, ...options } = {}) {
  const terminal = new Terminal(options);
  const renderer = Renderer.new(terminal._cols, terminal._rows);
  Object.defineProperties(this, {
    _memory: { value: memory },
    _terminal: { value: terminal },
    _renderer: { value: renderer },
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
  width: { value: app$width, writable: true, configurable: true },
  height: { value: app$height, writable: true, configurable: true },
  fontFamily: { value: app$fontFamily, writable: true, configurable: true },
  fontSize: { value: app$fontSize, writable: true, configurable: true },
  fontWeight: { value: app$fontWeight, writable: true, configurable: true },
  cellWidth: { value: app$cellWidth, writable: true, configurable: true },
  cellHeight: { value: app$cellHeight, writable: true, configurable: true },
  node: { value: app$node, writable: true, configurable: true },
});
