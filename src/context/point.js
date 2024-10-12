export function context_point(I, {x: X, y: Y, stroke: S}) {
  for (const i of I) {
    this.stroke(S[i]);
    this._renderer.point(X[i], Y[i]);
  }
  return this;
}
