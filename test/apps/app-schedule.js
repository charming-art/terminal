import { createApp, useFrame, clearable } from "./utils";

const TARGET_FRAME = 30;

export async function appSchedule() {
  const [update, clear] = useFrame(TARGET_FRAME);

  let x = 0;

  const app = await createApp({ cols: 10, rows: 3, frameRate: 20 });

  app
    .stroke("@")
    .frame(() => {
      const i = x % app.cols();
      const j = (x / app.cols()) | 0;
      app.scene("#000");
      app.translate(i, j);
      app.point(0, 0);
      x += 1;
      if (x > app.cols() * app.rows() - 1) app.stop();
    })
    .frame(() => {
      if (app.frameCount() > 10) app.frameRate(10);
      if (app.frameCount() === 15) app.stop().start();
      update(app.frameCount());
    })
    .start();

  return app.call(clearable, clear).node();
}

appSchedule.snap = TARGET_FRAME;
