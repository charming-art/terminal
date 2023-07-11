import { createTerminal } from "./utils";

export function terminalDouble() {
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

  const terminal = createTerminal({
    cols: n,
    rows: n,
    mode: "double",
    fontFamily: '"Fira Code", courier-new, courier, monospace, "Powerline Extra Symbols"',
  });
  terminal.background("#000");

  for (let i = 0; i < chars.length; i++) {
    const [char, fg, bg, wide] = chars[i];
    const x = i % n;
    const y = (i / n) | 0;
    terminal.char(char, x, y, fg, bg, wide);
  }

  return terminal.node();
}

terminalDouble.snap = true;
