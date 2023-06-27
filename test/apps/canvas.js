import { Canvas } from "@charming-art/charming-canvas";

export function canvas() {
  const canvas = new Canvas();
  canvas.background("black");
  window.canvas = canvas;
  return canvas.node();
}
