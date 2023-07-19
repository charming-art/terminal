import { after } from "./hooks.js";

export function app$point(x, y) {
  this._renderer.point(x, y);
  return this;
}

export const app$pixels = after(function (x, y, render) {
  const context = this._terminal._context;
  const px = x * this.cellWidth();
  const py = y * this.cellHeight();
  context.save();
  context.translate(px, py);
  render(context, this);
  context.restore();
  return this;
});
