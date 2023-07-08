import { createCanvas } from "./utils";

export function canvasSize() {
  const canvas = createCanvas({ width: 100, height: 60 });
  canvas.background("black");
  for (let i = 0; i < canvas.cols; i++) {
    for (let j = 0; j < canvas.rows; j++) {
      canvas.char("+", i, j, "#fff");
    }
  }
  return canvas.node();
}

canvasSize.snap = true;
