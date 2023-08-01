import { createApp } from "./utils";

export async function appAttributes() {
  const app = await createApp({ cols: 25, rows: 8 });

  app
    .call((app) => app.background("·", "#aaa"))
    .call((app) => app.stroke("@").fill("+", "steelblue").rect(0, 0, 5, 5))
    .call((app) => app.noStroke().fill("+", "orange").rect(8, 0, 5, 5).point(11, 11))
    .call((app) =>
      app
        .stroke("Q")
        .noFill()
        .fill("+", "yellow")
        .pushMatrix()
        .translate(19, 0)
        .rotate(Math.PI / 4)
        .rect(0, 0, 5, 5)
        .popMatrix()
    );

  return app.render().node();
}

appAttributes.snap = true;
