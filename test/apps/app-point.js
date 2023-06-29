import { app as createApp } from "@charming-art/charming";

export function appPoint() {
  const points = [
    [-1, -1, "@"],
    [0, 1, "@", "steelblue", "orange"],
    [1, 0, "+", "red", "yellow"],
    [3, 3, "@"],
  ];

  const app = createApp().size(3, 3).background("#000");

  for (const [x, y, ch, fg, bg] of points) {
    app.stroke(ch, fg, bg);
    app.point(x, y);
  }

  return app.render().node();
}

appPoint.snap = true;
