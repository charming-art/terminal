import { frameOf } from "../common.js";

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
