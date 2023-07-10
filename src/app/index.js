import { app$render, app$size } from "./structure.js";
import { app$background, app$stroke } from "./setting.js";
import { app$point } from "./primitive.js";
import { app$cols, app$rows, app$node } from "./control.js";

export function App(memory, options = {}) {
  Object.defineProperties(this, {
    _memory: { value: memory },
    _options: { value: options },
  });
}

Object.defineProperties(App.prototype, {
  size: { value: app$size, writable: true, configurable: true },
  render: { value: app$render, writable: true, configurable: true },
  stroke: { value: app$stroke, writable: true, configurable: true },
  background: { value: app$background, writable: true, configurable: true },
  point: { value: app$point, writable: true, configurable: true },
  cols: { get: app$cols, configurable: true },
  rows: { get: app$rows, configurable: true },
  node: { value: app$node, writable: true, configurable: true },
});
