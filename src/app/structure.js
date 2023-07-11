import { NULL_VALUE, CELL_SIZE } from "./constants";
import { Terminal } from "../terminal.js";
import { Renderer } from "../wasm/index.js";

export function app$size(cols = 80, rows = 24) {
  const [_cols, width] = maybePixel(cols);
  const [_rows, height] = maybePixel(rows);
  this._terminal = new Terminal({ ...this._options, cols: _cols, rows: _rows, width, height });
  this._cols = this._terminal.cols();
  this._rows = this._terminal.rows();
  this._renderer = Renderer.new(this._cols, this._rows);
  return this;
}

export function app$render() {
  if (this._fill) {
    this._terminal.background(this._fill);
    this._fill = null;
  }
  const bufferPtr = this._renderer.render();
  const buffer = new Uint32Array(this._memory.buffer, bufferPtr, this._cols * this._rows * CELL_SIZE);
  for (let i = 0; i < this._rows; i++) {
    for (let j = 0; j < this._cols; j++) {
      const index = (this._cols * i + j) * CELL_SIZE;
      const [ch, wch] = decodeChar(buffer[index]);
      const [ch1, wch1] = decodeChar(buffer[index + 1]);
      const fg = decodeColor(buffer[index + 2]);
      const bg = decodeColor(buffer[index + 3]);
      const wide = wch + wch1 >= 2;
      const ch2 = ch + ch1;
      if (ch2 || fg) this._terminal.char(ch2, j, i, fg, bg, wide);
    }
  }
  return this;
}

function decodeColor(color) {
  if (color === NULL_VALUE) return undefined;
  const r = (color & 0xff0000) >> 16;
  const g = (color & 0x00ff00) >> 8;
  const b = color & 0x0000ff;
  return `rgb(${r}, ${g}, ${b})`;
}

function decodeChar(n) {
  if (n === NULL_VALUE) return ["", 0];
  const first = n >> 31;
  const n1 = n & 0x0fffffff;
  const w = first === 0 ? 1 : 2;
  return [String.fromCodePoint(n1), w];
}

function maybePixel(size) {
  if (typeof size === "number") return [size, undefined];
  return [undefined, parseFloat(size)];
}
