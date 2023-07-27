import { hook } from "./hooks.js";

export function app$point(x, y) {
  this._renderer.point(x, y);
  return this;
}

export function app$line(x, y, x1, y1) {
  this._renderer.line(x, y, x1, y1);
  return this;
}

export const app$pixels = function (x, y, render) {
  const bufferPtr = this._renderer.transform(x, y);
  const buffer = new Float64Array(this._memory.buffer, bufferPtr, 3);
  const [tx, ty] = buffer;
  return hook(function () {
    const context = this._terminal._context;
    const px = tx * this.cellWidth();
    const py = ty * this.cellHeight();
    context.save();
    context.translate(px, py);
    render(context, this);
    context.restore();
  }, "after").call(this);
};
