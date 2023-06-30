import { color as rgb } from "d3-color";
import { Canvas } from "./canvas";
import { Rasterizer } from "../rasterizer/index";
import { memory } from "../rasterizer/index_bg.wasm";

const CELL_SIZE = 3;

// TODO Handle opacity.
function encodeColor(color) {
  if (color === -1) return -1;
  const { r, g, b } = rgb(color);
  return b + (g << 8) + (r << 16);
}

function encodeChar(ch) {
  return ch.codePointAt(0);
}

function decodeColor(color) {
  if (color === -1) return undefined;
  const r = (color & 0xff0000) >> 16;
  const g = (color & 0x00ff00) >> 8;
  const b = color & 0x0000ff;
  return `rgb(${r}, ${g}, ${b})`;
}

function decodeChar(ch) {
  return ch === -1 ? "" : String.fromCodePoint(ch);
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
  stroke(ch, fg = -1, bg = -1) {
    this._rasterizer.stroke(encodeChar(ch), encodeColor(fg), encodeColor(bg));
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
    const buffer = new Int32Array(memory.buffer, bufferPtr, this._cols * this._rows * CELL_SIZE);
    for (let i = 0; i < this._rows; i++) {
      for (let j = 0; j < this._cols; j++) {
        const index = (this._cols * i + j) * CELL_SIZE;
        const ch = buffer[index];
        const fg = buffer[index + 1];
        const bg = buffer[index + 2];
        this._renderer.char(decodeChar(ch), j, i, decodeColor(fg), decodeColor(bg));
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
