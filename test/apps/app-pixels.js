import { createApp } from "./utils";

export async function appPixels() {
  const app = await createApp({ cols: 9, rows: 9, mode: "double" });

  for (let i = 0; i < app.cols() * app.rows(); i++) {
    app.stroke(" ", "#fff", i % 2 === 0 ? "#000" : "#fff");
    app.point(i % app.cols(), (i / app.cols()) | 0);
  }

  app.pixels(5, 5, (context) => {
    const r = Math.max(app.cellWidth(), app.cellHeight()) / 2;
    context.fillStyle = "orange";
    context.beginPath();
    context.arc(-r, -r, r, 0, 2 * Math.PI);
    context.closePath();
    context.fill();
  });

  app.pixels(4, 4, (context, app) => {
    const r = Math.max(app.cellWidth(), app.cellHeight()) / 2;
    context.fillStyle = "steelblue";
    context.beginPath();
    context.arc(-r, -r, r, 0, 2 * Math.PI);
    context.closePath();
    context.fill();
  });

  return app.render().node();
}
