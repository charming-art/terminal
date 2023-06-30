import { app as createApp } from "@charming-art/charming";

export function appSize() {
  const app = createApp().size("100px", "60px").background("#000");
  app.stroke("+", "#fff");
  for (let i = 0; i < app.cols; i++) {
    for (let j = 0; j < app.rows; j++) {
      app.point(i, j);
    }
  }
  return app.render().node();
}

appSize.snap = true;
