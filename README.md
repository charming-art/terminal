# Charming: Character Art Programming

Charming is a creative code language for character art programming.

## Get Started

```js
import * as cm from "@charming-art/charming";

const app = await cm.app({ width: 100, height: 100 });

app.rect(0, 0, 20, 10);

app.render();
```

```js
import * as cm from "@charming-art/charming";

const app = await cm.app({ width: 100, height: 100 });

let x = 0;

app.draw(() => {
  app.rect(x, 0, 20, 20);
  x += 1;
});

app.render();
```
