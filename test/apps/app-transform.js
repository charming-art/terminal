import { createApp, background } from "./utils";

export async function appTransform() {
  const app = await createApp({ rows: 10, cols: 10 });

  app
    .scene("#4e79a7")
    .call(background, "+", "#76b7b2")
    .call((app) => app.stroke("O").point(1, 1))
    .call((app) => app.translate(1, 1).scale(2, 2))
    .call((app) => app.stroke("@").point(1, 1))
    .call((app) =>
      app
        .pushMatrix()
        .stroke("X")
        .rotate(Math.PI / 4)
        .point(1, 1)
        .popMatrix()
    )
    .call((app) => app.stroke("Q").point(1, 2))
    .pixels(2, 2, (context) => {
      context.fillStyle = "red";
      context.rect(0, 0, app.cellWidth(), app.cellHeight());
      context.fill();
    });

  return app.render().node();
}

appTransform.snap = true;
