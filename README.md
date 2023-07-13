# Charming: Character Art Programming

Charming is a creative code language for character art programming.

## Installing

> TODO

## A Simple Example

```js
import * as cm from "@charming-art/charming";

const app = await cm.app({ mode: "double" });

for (let t = 0; t <= Math.PI * 2; t += Math.PI / 120) {
  const x = app.cols() / 2 + 10 * Math.cos(t) * Math.cos(t * 3);
  const y = app.rows() / 2 + 10 * Math.sin(t) * Math.cos(t * 3);
  app.stroke(cm.wide("🌟"));
  app.point(x, y);
}

document.body.append(app.render().node());
```

<img src="./img/star.png" width="100%" alt="star">

## API Reference

- [Creating Application](#creating-application)
- [Adding Shapes](#adding-shapes)
- [Setting Attributes](#setting-attributes)
- [Binding Data](#binding-data)
- [Manipulating Colors](#manipulating-colors)
- [Applying Transformations](#applying-transformations)
- [Organizing Context](#organizing-context)
- [Handling Events](#handling-events)
- [Control Flow](#control-flow)
- [Getting Variables](#getting-variables)
- [Math Extension](#math-extension)

### Creating Application

> TODO

### Adding Shapes

> TODO

### Setting Attributes

> TODO

### Binding Data

> TODO

### Manipulating Colors

> TODO

### Applying Transformations

> TODO

### Organizing Context

> TODO

### Handling Events

> TODO

### Control Flow

> TODO

### Getting Variables

> TODO

### Math Extension

> TODO
