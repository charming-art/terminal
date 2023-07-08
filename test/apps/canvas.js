import { createCanvas } from "./utils";

export function canvas() {
  const canvas = createCanvas();
  canvas.background("black");
  return canvas.node();
}
