import { color as rgb } from "d3-color";
import { hook } from "./hooks.js";
import { NULL_VALUE } from "./constants.js";

export const app$scene = hook(function (color) {
  this._terminal.background(color);
}, "before");

export function app$stroke(ch, fg = "#ffffff", bg = null) {
  const [n, n1 = NULL_VALUE] = encodeChar(ch);
  this._renderer.stroke(n, n1, encodeColor(fg), encodeColor(bg));
  return this;
}

function encodeColor(color) {
  if (color === NULL_VALUE || color === null) return NULL_VALUE;
  const { r, g, b } = rgb(color);
  return b + (g << 8) + (r << 16);
}

function encodeChar(ch) {
  if (Array.isArray(ch)) return ch;
  return Array.from(ch)
    .slice(0, 2)
    .map((ch) => ch.codePointAt(0));
}
