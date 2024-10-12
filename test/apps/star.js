import * as cm from "@charming-art/terminal";

export async function Star() {
  const context = await new cm.Context().init({mode: "double", width: 520, height: 520});
  const I = Array.from({length: 240}, (_, i) => i);
  const A = I.map((i) => (i / 240) * 2 * Math.PI);
  const X = A.map((t) => context.cols() / 2 + 12 * Math.cos(t) * Math.cos(t * 3));
  const Y = A.map((t) => context.rows() / 2 + 12 * Math.sin(t) * Math.cos(t * 3));
  const S = I.map(() => cm.wide("🌟"));
  context.point(I, {x: X, y: Y, stroke: S});
  return context.render();
}
