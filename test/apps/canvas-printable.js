import { Canvas } from "@charming-art/charming-canvas";

export function canvasPrintable() {
  const cols = 19;
  const rows = 5;

  const canvas = new Canvas({
    cols,
    rows,
    fontSize: 15,
    fontFamily: '"Fira Code", courier-new, courier, monospace, "Powerline Extra Symbols"',
  });
  canvas.background("#4e79a7");

  const start = 33;
  const end = 127;
  for (let i = start; i < end; i++) {
    const j = i - start;
    const x = j % cols;
    const y = (j / cols) | 0;
    canvas.char(String.fromCodePoint(i), x, y, "yellow", i % 2 === 0 ? "#4e79a7" : "#76b7b2");
  }

  return canvas.node();
}

canvasPrintable.snap = true;
