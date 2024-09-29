# Charming Cell

```js
import * as Cell from "@charming-art/cell";

function App(ctx) {
  let x = 0;
  return {
    setup() {
      ctx.size(30, 20);
    },
    draw() {
      ctx.background(" ");
      ctx.fill("@", "red", "yellow");
      ctx.rect(x, 0, 10, 5);
      x += 1;
    },
  };
}

document.body.append(await Cell.render(App));
```
