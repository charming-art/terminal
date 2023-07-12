import { createApp } from "./utils";

export async function appPoint() {
  const points = [
    [-1, -1, "@"],
    [0, 1, "@", "steelblue", "orange"],
    [1, 0, "+", "red", "yellow"],
    [3, 3, "@"],
  ];

  const app = await createApp();

  app.size(3, 3);

  for (const [x, y, ch, fg, bg] of points) {
    app.stroke(ch, fg, bg);
    app.point(x, y);
  }

  return app.render().node();
}

appPoint.snap = true;
