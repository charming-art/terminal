import * as Cell from "@charming-art/cell";

export function Star(ctx) {
  return {
    mode: "double",
    width: 520,
    height: 520,
    setup() {
      for (let t = 0; t <= Math.PI * 2; t += Math.PI / 120) {
        const x = ctx.cols() / 2 + 12 * Math.cos(t) * Math.cos(t * 3);
        const y = ctx.rows() / 2 + 12 * Math.sin(t) * Math.cos(t * 3);
        ctx.stroke(Cell.wide("🌟"));
        ctx.point(x, y);
      }
    },
  };
}
