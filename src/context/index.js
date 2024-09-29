import {context_init} from "./init.js";
import {context_run} from "./run.js";
import {context_stroke} from "./stroke.js";
import {context_point} from "./point.js";
import {context_setup} from "./setup.js";
import {context_rows} from "./rows.js";
import {context_cols} from "./cols.js";
import {context_node} from "./node.js";

export function Context() {
  Object.defineProperties(this, {
    _memory: {value: null, writable: true},
    _terminal: {value: null, writable: true},
    _renderer: {value: null, writable: true},
    _setup: {value: null, writable: true},
  });
}

Object.defineProperties(Context.prototype, {
  setup: {value: context_setup, writable: true, configurable: true},
  init: {value: context_init, writable: true, configurable: true},
  run: {value: context_run, writable: true, configurable: true},
  stroke: {value: context_stroke, writable: true, configurable: true},
  point: {value: context_point, writable: true, configurable: true},
  rows: {value: context_rows, writable: true, configurable: true},
  cols: {value: context_cols, writable: true, configurable: true},
  node: {value: context_node, writable: true, configurable: true},
});
