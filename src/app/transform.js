export function app$translate(x, y) {
  this._renderer.translate(x, y);
  return this;
}

export function app$scale(x, y) {
  this._renderer.scale(x, y);
  return this;
}

export function app$rotate(theta) {
  this._renderer.rotate(theta);
  return this;
}

export function app$pushMatrix() {
  this._renderer.pushMatrix();
  return this;
}

export function app$popMatrix() {
  this._renderer.popMatrix();
  return this;
}
