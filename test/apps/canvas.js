import { Canvas } from "@charming-art/charming-canvas";

export default function () {
  const canvas = new Canvas();
  canvas.background("black");
  window.canvas = canvas;
  return canvas.node();
}
