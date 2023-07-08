import { createCanvas } from "./utils";

export function canvasDouble() {
  const chars = [
    ["💯", undefined, undefined, true],
    ["a", "#fff", "steelblue"],
    ["🤩", undefined, undefined, true],
    ["b", "#fff", "steelblue"],
    ["𠮷", undefined, undefined, true],
    ["c", "#fff", "steelblue"],
    ["中", undefined, undefined, true],
    ["d", "#fff", "steelblue"],
    ["文", undefined, undefined, true],
  ];
  const n = 3;

  const canvas = createCanvas({
    cols: n,
    rows: n,
    mode: "double",
    fontFamily: '"Fira Code", courier-new, courier, monospace, "Powerline Extra Symbols"',
  });
  canvas.background("#000");

  for (let i = 0; i < chars.length; i++) {
    const [char, fg, bg, wide] = chars[i];
    const x = i % n;
    const y = (i / n) | 0;
    canvas.char(char, x, y, fg, bg, wide);
  }

  return canvas.node();
}

canvasDouble.snap = true;
