# Charming: Character Computing

**Charming** is a free, open-source, creative code language for character computing, which means drawing characters in a terminal-like application driven by computational algorithm. It is embedded in JavaScript and uses a software renderer written in Rust compiled to WASM, to gain high performance hopefully. It has an concise, inclusive, yet expressive API inspired by [Processing](https://processing.org/) or [P5.js](https://p5js.org/).

Charming focus on making the _charm_ of [_character_](<https://en.wikipedia.org/wiki/Character_(symbol)>) and [_computing_](https://en.wikipedia.org/wiki/Computing) accessible for artists, designers, educators, beginners, and anyone else! Our hope with Charming is that you spend less time wrangling the machinery of programming and more time "using character and computing to tell stories". Or put more simply: **with Charming, you'll express more, more easily.**

If you are new to Charming, we highly recommend first reading these tutorials to introduce Charming's core concepts:

- [Creating Application](#creating-application-1) - Rendering app into DOM and animate it.
- [Setting Attributes](#setting-attributes-1) - Controlling the aesthetic appearance of the shapes.
- [Drawing Shapes](#drawing-shapes-1) - Adding primitives, vertices, and curves to app.
- [Applying Transformations](#applying-transformations-1) - Transforming shapes.
- [Control Flow](#control-flow-1) - A more declarative programming style.
- [Instance Properties](#instance-properties-1) - State of the app.

And there are [a plenty of examples](https://github.com/charming-art/charming/tree/next) to get started with.

## Installing

Charming is typically installed via a package manager such as Yarn or NPM.

```bash
yarn add @charming-art/charming
```

```bash
npm install @charming-art/charming
```

Charming can then imported as a namespace:

```js
import * as cm from "@charming-art/charming";
```

In vanilla HTML, Charming can be imported as an ES module, say from jsDelivr:

```html
<script type="module">
  import * as cm from "https://cdn.jsdelivr.net/npm/@charming-art/charming@0.1/+esm";

  const app = await cm.app();

  // ...

  document.body.append(app.render().node());
</script>
```

Charming is also available as a UMD bundle for legacy browsers.

```html
<script src="https://cdn.jsdelivr.net/npm/@charming-art/charming@0.1"></script>
<script>
  (async () => {
    const app = await cm.app();

    // ...

    document.body.append(app.render().node());
  })();
</script>
```

## A Simple Example

Here is a simple Charming example:

```js
const app = await cm.app({ mode: "double" });

for (let t = 0; t <= Math.PI * 2; t += Math.PI / 120) {
  const x = app.cols() / 2 + 10 * Math.cos(t) * Math.cos(t * 3);
  const y = app.rows() / 2 + 10 * Math.sin(t) * Math.cos(t * 3);
  app.stroke(cm.wide("🌟"));
  app.point(x, y);
}

document.body.append(app.render().node());
```

If Charming is properly installed, you should get a _lucky clove_ as below 🎉:

<img src="./img/star.png" width="100%" alt="star">

## API Reference

### [Creating Application](#creating-application-1)

Rendering app into DOM and animate it.

- [cm.**app**](#cm-app)
- [app.**render**](#app-render)
- [app.**frame**](#app-frame)
- [app.**start**](#app-start)
- [app.**stop**](#app-stop)

### [Setting Attributes](#setting-attributes-1)

Controlling the aesthetic appearance of the shapes.

- [app.**scene**](#app-scene)
- [app.**background**](#app-background)
- [app.**stroke**](#app-stroke)
- [app.**noStroke**](#app-nostroke)
- [app.**fill**](#app-fill)
- [app.**noFill**](#app-nofill)
- [cm.**wide**](#cm-wide)

### [Drawing Shapes](#drawing-shapes-1)

Adding primitives, vertices, and curves to app.

- [app.**point**](#app-point)
- [app.**line**](#app-line)
- [app.**rect**](#app-rect)
- [app.**pixels**](#app-pixels)

### [Applying Transformations](#applying-transformations-1)

Transforming shapes.

- [app.**translate**](#app-translate)
- [app.**scale**](#app-scale)
- [app.**rotate**](#app-rotate)
- [app.**popMatrix**](#app-popMatrix)
- [app.**pushMatrix**](#app-pushMatrix)

### [Control Flow](#control-flow-1)

A more declarative programming style.

- [app.**call**](#app-call)

### [Instance Properties](#instance-properties-1)

State of the app.

- [app.**node**](#app-node)
- [app.**cols**](#app-cols)
- [app.**rows**](#app-rows)
- [app.**width**](#app-width)
- [app.**height**](#app-height)
- [app.**cellWidth**](#app-cellwidth)
- [app.**cellHeight**](#app-cellheight)
- [app.**fontSize**](#app-fontsize)
- [app.**fontFamily**](#app-fontfamily)
- [app.**fontWeight**](#app-fontweight)
- [app.**frameCount**](#app-frameCount)
- [app.**frameRate**](#app-frameRate)

## Creating Application

<a name="cm-app" href="#cm-app">#</a> cm.**app**(_[options]_)

```js
const app = await cm.app(options);
```

- **cols**
- **rows**
- **width**
- **height**
- **fontSize**
- **fontWeight**
- **fontFamily**
- **mode**

<a name="app-render" href="#app-render">#</a> app.**render**()

```js
app.render();
```

<a name="app-frame" href="#app-frame">#</a> app.**frame**()

```js
let x = 0;
app.frame(() => {
  app.point(x, x);
  x++;
});
```

<a name="app-start" href="#app-start">#</a> app.**start**()

```js
app.start();
```

<a name="app-stop" href="#app-stop">#</a> app.**stop**()

```js
app.stop();
```

## Setting Attributes

<a name="app-scene" href="#app-scene">#</a> app.**scene**(_color_)

```js
app.scene("#000000");
```

<a name="app-background" href="#app-background">#</a> app.**background**(_ch[, fg[, bg]]_)

> WIP

```js
app.background("@", "steelblue", "orange");
```

<a name="app-stroke" href="#app-stroke">#</a> app.**stroke**(_ch[, fg[, bg]]_)

```js
app.stroke("@", "steelblue", "orange");
```

<a name="app-nostroke" href="#app-nostroke">#</a> app.**noStroke**()

> WIP

```js
app.noStroke();
```

<a name="app-fill" href="#app-fill">#</a> app.**fill**(_ch[, fg[, bg]]_)

> WIP

```js
app.fill("@", "steelblue", "orange");
```

<a name="app-nofill" href="#app-nofill">#</a> app.**noFill**()

> WIP

```js
app.noFill();
```

<a name="cm-wide" href="#cm-wide">#</a> cm.**wide**(_ch_)

```js
cm.wide("🚀");
```

## Drawing Shapes

<a name="app-point" href="#app-point">#</a> app.**point**(_x, y_)

```js
app.point(0, 0);
```

<a name="app-line" href="#app-line">#</a> app.**line**(_x, y, x1, y1_)

```js
app.line(0, 0, 10, 10);
```

<a name="app-rect" href="#app-rect">#</a> app.**rect**(_x, y, width, height_)

```js
app.rect(0, 0, 10, 10);
```

<a name="app-pixels" href="#app-pixels">#</a> app.**pixels**(_x, y, render_)

```js
for (let i = 0; i < app.cols() * app.rows(); i++) {
  app.stroke(" ", "#fff", i % 2 === 0 ? "#000" : "#fff");
  app.point(i % app.cols(), (i / app.cols()) | 0);
}

app.pixels(5, 5, (context) => {
  const r = Math.max(app.cellWidth(), app.cellHeight()) / 2;
  context.fillStyle = "orange";
  context.beginPath();
  context.arc(-r, -r, r, 0, 2 * Math.PI);
  context.closePath();
  context.fill();
});
```

## Applying Transformations

<a name="app-translate" href="#app-translate">#</a> app.**translate**(_x, y_)

```js
app.translate(10, 10);
```

<a name="app-scale" href="#app-scale">#</a> app.**scale**(_sx, sy_)

```js
app.scale(2, 2);
```

<a name="app-rotate" href="#app-rotate">#</a> app.**rotate**(_theta_)

```js
app.rotate(Math.PI / 2);
```

<a name="app-pushMatrix" href="#app-pushMatrix">#</a> app.**pushMatrix**()

```js
app.pushMatrix();
```

<a name="app-popMatrix" href="#app-popMatrix">#</a> app.**popMatrix**()

```js
app.popMatrix();
```

## Control Flow

For advance usage, apps provide methods for custom control flow.

<a name="app-call" href="#app-call">#</a> app.**call**(_function[, arguments…]_)

Calls the specified _function_ on this app with any optional _arguments_ and returns this app. This is equivalent to calling the function by hand but avoids to break method chaining. For example, to set the color of every cells in a reusable function:

```js
function background(app, ch, fg) {
  app.stroke(ch, fg);
  for (let i = 0; i < app.cols(); i++) {
    for (let j = 0; j < app.rows(); j++) {
      app.point(i, j);
    }
  }
}
```

It breaks the method chaining between _app.scene_ and _app.render_:

```js
app.scene("#4e79a7");
background(app, "+", "#76b7b2"); // Breaks method chaining!
app.render();
```

Now say:

```js
app
  .scene("#4e79a7")
  .call(background, "+", "#76b7b2") // Facilitates the method chaining.
  .render();
```

## Instance Properties

For convince, apps provide methods to get some of instance properties.

<a name="app-node" href="#app-node">#</a> app.**node**()

Returns the canvas used to render the app. For example, to mount the rendered app to a specific DOM.

```js
const root = document.getElementById("id");
root.append(app.node());
```

<a name="app-cols" href="#app-cols">#</a> app.**cols**()

Returns the number of columns in the terminal. For example, to draw a point at the center of the terminal:

```js
app.point(app.cols() / 2, app.rows() / 2);
```

<a name="app-rows" href="#app-rows">#</a> app.**rows**()

Returns the number of rows in the terminal. For example, to draw a point at th center of the terminal:

```js
app.point(app.cols() / 2, app.rows() / 2);
```

<a name="app-width" href="#app-width">#</a> app.**width**()

Returns the computed width of the terminal, which satisfies the following constraint:

```js
app.width() === app.cols() * app.cellWidth();
```

<a name="app-height" href="#app-height">#</a> app.**height**()

Returns the computed height of the terminal, which satisfies the following constraint:

```js
app.height() === app.rows() * app.cellHeight();
```

<a name="app-cellwidth" href="#app-cellwidth">#</a> app.**cellWidth**()

Returns the computed width of the cells, which satisfies the following constraint:

```js
app.cellWidth() === app.width() / app.cols();
```

<a name="app-cellheight" href="#app-cellheight">#</a> app.**cellHeight**()

Returns the computed height of the cells, which satisfies the following constraint:

```js
app.cellHeight() === app.height() / app.rows();
```

<a name="app-fontsize" href="#app-fontsize">#</a> app.**fontSize**()

Returns the font size used to render text. For example, to get the default font size:

```js
const app = await cm.app();
app.fontSize(); // 15
```

<a name="app-fontweight" href="#app-fontweight">#</a> app.**fontWeight**()

Returns the font weight used to render text. For example, to get the default font weight:

```js
const app = await cm.app();
app.fontWeight(); // "normal"
```

<a name="app-fontfamily" href="#app-fontfamily">#</a> app.**fontFamily**()

Returns the font family used to render text. For example, to get the default font family:

```js
const app = await cm.app();
app.fontFamily(); // "courier-new, courier, monospace"
```

<a name="app-frameCount" href="#app-frameCount">#</a> app.**frameCount**()

```js
app.frameCount();
```

<a name="app-frameRate" href="#app-frameRate">#</a> app.**frameRate**(_[rate]_)

```js
app.frameRate(10);
app.frameRate(); // 10
```
