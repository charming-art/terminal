import { frameOf } from "../common.js";
import { app as App } from "@charming-art/charming";
import { Canvas } from "@charming-art/charming-canvas";

export async function createApp(options) {
  const app = await App(options);
  window.app = app;
  return app;
}

export function createCanvas(options) {
  const canvas = new Canvas(options);
  window.canvas = canvas;
  return canvas;
}

export function useFrame(TARGET_FRAME, stop) {
  let frame = 0;
  let div;
  const update = () => {
    if (!div) {
      div = document.createElement("div");
      document.body.insertBefore(div, null);
      div.innerText = frameOf(frame);
    }
    frame++;
    if (frame >= TARGET_FRAME && import.meta.env.MODE !== "development") stop();
    div.innerText = `frame: ${frame}`;
  };
  const clear = () => {
    if (div) div.remove();
  };
  return [update, clear];
}
