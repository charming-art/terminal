import { app } from "@charming-art/charming";
import { Terminal } from "@charming-art/charming-terminal";

export function noop() {
  window.createApp = app;
  window.Terminal = Terminal;
  return null;
}
