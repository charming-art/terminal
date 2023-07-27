import { createApp } from "./utils";

export async function appSize() {
  const app = await createApp({ width: 100, height: 60 });
  app.scene("#4e79a7").background("+", "#76b7b2");
  return app.render().node();
}

appSize.snap = true;
