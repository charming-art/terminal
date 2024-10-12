# Charming Terminal

The terminal renderer for Charming.

> [!NOTE]
> The current next branch is implementing the new proposal API for production use. Please refer to the [python branch](https://github.com/charming-art/charming-cell/tree/python) for the released Python version.

## Get started

```js
import * as cm from "@charming-art/terminal";

const context = await new cm.Context().init({mode: "double", width: 520, height: 520});
const I = Array.from({length: 240}, (_, i) => i);
const A = I.map((i) => (i / 240) * 2 * Math.PI);
const X = A.map((t) => context.cols() / 2 + 12 * Math.cos(t) * Math.cos(t * 3));
const Y = A.map((t) => context.rows() / 2 + 12 * Math.sin(t) * Math.cos(t * 3));
const S = I.map(() => cm.wide("🌟"));
context.point(I, {x: X, y: Y, stroke: S});

document.body.append(context.render());
```

## License 📄

ISC@Bairui SU
