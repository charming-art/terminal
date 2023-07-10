import { color as rgb } from "d3-color";
import { NULL_VALUE } from "./constant";

export function app$canvasFill(color) {
  this._fill = color;
  return this;
}

export function app$stroke(ch, fg = NULL_VALUE, bg = NULL_VALUE) {
  const [n, n1 = NULL_VALUE] = encodeChar(ch);
  this._rasterizer.stroke(n, n1, encodeColor(fg), encodeColor(bg));
  return this;
}

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
