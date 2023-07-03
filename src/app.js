import { color as rgb } from "d3-color";
import { Canvas } from "./canvas";
import { Rasterizer } from "../rasterizer/index";
import { memory } from "../rasterizer/index_bg.wasm";
import { NULL_VALUE, CELL_SIZE } from "./constant";

// TODO Handle opacity.
function encodeColor(color) {
  if (color === NULL_VALUE) return NULL_VALUE;
  const { r, g, b } = rgb(color);
  return b + (g << 8) + (r << 16);
}

function encodeChar(ch) {
  if (Array.isArray(ch)) return ch;
  return Array.from(ch)
    .slice(0, 2)
    .map((ch) => ch.codePointAt(0));
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

class App {
  constructor(options = {}) {
    this._options = options;
  }
  size(cols = 80, rows = 24) {
    const [_cols, width] = maybePixel(cols);
    const [_rows, height] = maybePixel(rows);
    this._renderer = new Canvas({ cols: _cols, rows: _rows, width, height, ...this._options });
    this._cols = this._renderer.cols;
    this._rows = this._renderer.rows;
    this._rasterizer = Rasterizer.new(this._cols, this._rows);
    return this;
  }
  stroke(ch, fg = NULL_VALUE, bg = NULL_VALUE) {
    const [n, n1 = NULL_VALUE] = encodeChar(ch);
    this._rasterizer.stroke(n, n1, encodeColor(fg), encodeColor(bg));
    return this;
  }
  point(x, y) {
    this._rasterizer.point(x, y);
    return this;
  }
  background(color) {
    this._renderer.background(color);
    return this;
  }
  render() {
    const bufferPtr = this._rasterizer.render();
    const buffer = new Uint32Array(memory.buffer, bufferPtr, this._cols * this._rows * CELL_SIZE);
    for (let i = 0; i < this._rows; i++) {
      for (let j = 0; j < this._cols; j++) {
        const index = (this._cols * i + j) * CELL_SIZE;
        const n = buffer[index];
        const n1 = buffer[index + 1];
        const fg = buffer[index + 2];
        const bg = buffer[index + 3];
        const [ch, wch] = decodeChar(n);
        const [ch1, wch1] = decodeChar(n1);
        const wide = wch + wch1 >= 2;
        this._renderer.char(ch + ch1, j, i, decodeColor(fg), decodeColor(bg), wide);
      }
    }
    return this;
  }
  get cols() {
    return this._cols;
  }
  get rows() {
    return this._rows;
  }
  node() {
    return this._renderer.node();
  }
}

export function app(options) {
  return new App(options);
}
