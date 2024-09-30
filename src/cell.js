import {Context} from "./context/index.js";

export async function cell(App) {
  const ctx = new Context();
  const {setup, ...options} = App(ctx);
  await ctx.init(options);
  ctx.setup(setup);
  ctx.run();
  return ctx.node();
}
