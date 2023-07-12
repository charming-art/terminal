import { createTerminal } from "./utils";

export function terminalPrintable() {
  const cols = 19;
  const rows = 5;

  const terminal = createTerminal({
    cols,
    rows,
    fontSize: 15,
    fontWeight: "bold",
    fontFamily: '"Fira Code", courier-new, courier, monospace, "Powerline Extra Symbols"',
  });
  terminal.background("#4e79a7");

  const start = 33;
  const end = 127;
  for (let i = start; i < end; i++) {
    const j = i - start;
    const x = j % cols;
    const y = (j / cols) | 0;
    terminal.char(String.fromCodePoint(i), x, y, "yellow", i % 2 === 0 ? "#4e79a7" : "#76b7b2");
  }

  return terminal.node();
}

terminalPrintable.snap = true;
