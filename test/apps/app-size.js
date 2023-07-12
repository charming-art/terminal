import { createApp } from "./utils";

export async function appSize() {
  const app = await createApp();

  app.size("100px", "60px").scene("#4e79a7").stroke("+", "#76b7b2");

  for (let i = 0; i < app.cols(); i++) {
    for (let j = 0; j < app.rows(); j++) {
      app.point(i, j);
    }
  }

  return app.render().node();
}

appSize.snap = true;
