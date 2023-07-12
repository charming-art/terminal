import { createApp, useFrame } from "./utils";

const TARGET_FRAME = 2;

let timer;
const [update, clear] = useFrame(TARGET_FRAME, () => {
  clearInterval(timer);
});

export async function appInterval1() {
  const app = await createApp();

  // Setup
  let x = 0;
  app.size(10, 3);
  app.stroke("@");

  // Draw
  timer = setInterval(() => {
    const i = x % app.cols();
    const j = (x / app.cols()) | 0;
    app.point(i, j);
    app.render();
    x += 1;
    update();
    if (x > app.cols() * app.rows() - 1) clearInterval(timer);
  }, 100);

  const node = app.node();
  node.clear = () => {
    clearInterval(timer);
    clear();
  };
  return node;
}

appInterval1.snap = TARGET_FRAME;
