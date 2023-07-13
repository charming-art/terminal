import { wide } from "@charming-art/charming";
import { createApp } from "./utils";

export async function appDouble() {
  const chars = [
    [" +", "-", "+ "],
    [" |", wide("🚀"), "| "],
    [" +", "-", "+ "],
  ];

  const app = await createApp({ mode: "double", cols: 3, rows: 3 });

  for (let i = 0; i < chars.length; i++) {
    const row = chars[i];
    for (let j = 0; j < row.length; j++) {
      const ch = row[j];
      app.stroke(ch);
      app.point(j, i);
    }
  }

  return app.render().node();
}

appDouble.snap = true;
