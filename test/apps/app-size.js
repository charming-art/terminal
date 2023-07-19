import { createApp } from "./utils";

function background(app, ch, fg) {
  app.stroke(ch, fg);
  for (let i = 0; i < app.cols(); i++) {
    for (let j = 0; j < app.rows(); j++) {
      app.point(i, j);
    }
  }
}

export async function appSize() {
  const app = await createApp({ width: 100, height: 60 });
  app.scene("#4e79a7").call(background, "+", "#76b7b2");
  return app.render().node();
}

appSize.snap = true;
