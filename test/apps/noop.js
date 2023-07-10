import { app } from "@charming-art/charming";
import { Canvas } from "@charming-art/charming-canvas";

export function noop() {
  window.createApp = app;
  window.Canvas = Canvas;
  return null;
}
