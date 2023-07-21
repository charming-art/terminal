import { createApp, useFrame, clearable } from "./utils";

const TARGET_FRAME = 2;

export async function appSchedule1() {
  const [update, clear] = useFrame(TARGET_FRAME);

  let x = 0;

  const app = await createApp({ cols: 10, rows: 3, frameRate: 10 });

  app
    .stroke("@")
    .frame(() => {
      const i = x % app.cols();
      const j = (x / app.cols()) | 0;
      app.point(i, j);
      x += 1;
      if (x > app.cols() * app.rows() - 1) app.stop();
    })
    .frame(() => update())
    .start();

  return app.call(clearable, clear).node();
}

appSchedule1.snap = TARGET_FRAME;
