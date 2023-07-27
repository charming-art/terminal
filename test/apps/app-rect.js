import { createApp, background } from "./utils";

export async function appRect() {
  const app = await createApp({ cols: 6, rows: 6 });

  app.call(background, "·", "#aaa").call((app) => {
    app.stroke("@");
    app.rect(0, 0, 5, 5).rect(5, 0, 1, 0).rect(5, 5, 0, 0).rect(0, 5, 1, 1);
  });

  return app.render().node();
}

appRect.snap = true;
