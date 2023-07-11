import { createTerminal } from "./utils";

export function terminalSize() {
  const terminal = createTerminal({ width: 100, height: 60 });
  terminal.background("black");
  for (let i = 0; i < terminal.cols(); i++) {
    for (let j = 0; j < terminal.rows(); j++) {
      terminal.char("+", i, j, "#fff");
    }
  }
  return terminal.node();
}

terminalSize.snap = true;
