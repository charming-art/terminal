import { createApp, background } from "./utils";

export async function appLine() {
  const app = await createApp({ cols: 15, rows: 15 });

  app
    .call(background, "·", "#aaa")
    .call((app) => app.translate(Math.floor(app.cols() / 2), Math.floor(app.rows() / 2)))
    .call((app) => {
      const count = 16;
      for (let i = 0; i < count; i++) {
        const t = (i * Math.PI * 2) / count;
        const r = (i * (255 / count)) | 0;
        const g = (i % 2) * 255;
        app.pushMatrix();
        app.rotate(t);
        app.stroke("@", `rgb(${r}, ${g}, 255)`);
        app.line(0, 0, 5, 0);
        app.point(0, 0);
        app.popMatrix();
      }
    });

  return app.render().node();
}

appLine.snap = true;
