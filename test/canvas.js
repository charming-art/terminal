import { Canvas } from "@charming-art/charming-canvas";

export default function () {
  const start = 33;
  const end = 127;
  const cols = 20;
  const rows = 5;
  const canvas = new Canvas({
    cols,
    rows,
    fontSize: 20,
    background: "#eee",
  });
  for (let i = start; i < end; i++) {
    const j = i - start;
    const x = j % cols;
    const y = (j / cols) | 0;
    canvas.char(String.fromCodePoint(i), x, y, {
      color: "yellow",
      background: i % 2 === 0 ? "#eee" : "#aaa",
    });
  }
  return canvas.node();
}
