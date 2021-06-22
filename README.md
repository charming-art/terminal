# Charming

Charming is a creative coding language designed for **Character Terminal Art Programming**.

It is currently written in Python and provides Processing-like APIs, which aims to help artists, designers, educators, beginners, and anyone else to easily create following visual effects in terminal.

- [ASCII Art Animation](./docs/examples/overview.md#ASCII-Art-Animation)
- [Character-Style Generative Art](./docs/examples/overview.md#Character-Style-Generative-Art)
- [Terminal Game Application](./docs/examples/overview.md#Terminal-Game-Application)
- [Expressive Data Visualization](./docs/examples/overview.md#Expressive-Data-Visualization)

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/home_code.png" alt="Charming" height="320">&emsp;<img src="https://raw.githubusercontent.com/charming-art/public-files/master/welcome.gif" alt="Charming" height="320">

## 📎 Links

- [Introduction](https://observablehq.com/@pearmini/charming)
- [Tutorials](./docs/tutorials/readme.md)
- [API Reference](./docs/api/readme.md)
- [Examples](./docs/examples/readme.md)
- [Processing/P5.js to Charming](./docs/migrate.md)
- [Contributing](./CONTRIBUTING.md)
- [Future Work](https://github.com/charming-art/charming/projects/6)

## ⁉ Why is it

There are [many reasons](./docs/why-is-it.md) for creating Charming, but the most important one is that **I hope not only does Charming make you love programming for fun or show a magic world to you, but also make this journey relaxing and interesting**.

With the help of artificial intelligence, computer science and software engineering gaining more and more attention and so does Python, a large number of people choose to learn Python to make a living, but programming are far more than that.

Just like most of us do not play basketball for career purpose, we could consider programming as a new kind of hobby. **Because life can be without machine learning, web crawler or automated operations, but it can not be without creating and sharing things to have fun and to be present.**

![charm](https://raw.githubusercontent.com/charming-art/public-files/master/charm.png)

## ✨ Features

- **Highly Expressive**: Unlike traditional drawing system or tool using three numerical channels (`(r, g, b)` or `(h, s, v)`) to describe a color, Charming allows you to describe a color like `(character, foreground color, background color)`, which means you can express more with the extra the `character` channel. Please see [Covid-19 Bar Chart](./docs/examples/barchart.md) as an example.
- **Powerful and Flexible**: Charming is not as same as [urwid](https://github.com/urwid/urwid) or [click](https://github.com/pallets/click) to build console line interface. Actually it more like [asciimatics](https://github.com/peterbrittain/asciimatics), [art](https://github.com/sepandhaghighi/art) or [tcharts](https://github.com/ProtoTeam/tcharts.js) to draw some visual effects in the terminal but with more flexibility. Instead of drawing limited and predefined shapes or effects, you can draw some basic primitives, custom shapes, curves, images, typography with transforms (translate, rotate, shear) and even events (mouse, keyboard) in Charming. Please see [Heart](./docs/examples/heart.md) and [Eating Poetry Game](./docs/examples/snake.md) as examples.
- **Easy to Learn and Use**: Charming is very beginner-friendly, because of Python's simple syntax and [Processing](https://processing.org/)'s concise APIs. It will be more easier if you are already familiar with them. Once you've master Charming, you can create anything interesting in you head with it and enjoy the pure joy of coding.

|  [Art of Heart](./docs/examples/heart.md)   |  [Eating Poetry Game](./docs/examples/snake.md) |  [Covid-19 Bar Chart](./docs/examples/barchart.md) |
|  :--:  |  :--: | :--:  |
| <img src="https://raw.githubusercontent.com/charming-art/public-files/master/example_heart.gif" height="180px" alt="heart" />|<img src="https://raw.githubusercontent.com/charming-art/public-files/master/example_snake.gif" alt="snake" height="180px" />|<img src="https://raw.githubusercontent.com/charming-art/public-files/master/barchart.png" height="180px" alt="bar chart" /> |

## 📦 Installation

- **Supported OS**: Charming currently only supports **MacOS**, though it should also work for any other platform that provides a working [curses](https://docs.python.org/3/howto/curses.html) implementation. It soon will support **Windows** and run in **Modern Browsers**.
- **Python**: 3.6/3.7/3.8

```bash
$ pip3 install charming --user
```

## 📺 A Simple Example

```python
# rect.py

import charming as cm

# draw a rect
cm.full_screen()
cm.rect(0, 0, 10, 10)

# run the sketch
cm.run()
```

```bash
$ python3 rect.py
```

![get started](https://raw.githubusercontent.com/charming-art/public-files/master/get_started.png)
