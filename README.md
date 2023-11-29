# Pycharming: Character Terminal Art Programing

Pycharming is a creative coding language designed for **Character Terminal Art Programming**.

It is currently written in Python and provides Processing-like APIs, which aims to help artists, designers, educators, beginners, and anyone else to easily create following visual effects in terminal.

- [ASCII Art Animation](./docs/examples/readme.md#ASCII-Art-Animation)
- [Character-Style Generative Art](./docs/examples/readme.md#Character-Style-Generative-Art)
- [Terminal Game Application](./docs/examples/readme.md#Terminal-Game-Application)
- [Expressive Data Visualization](./docs/examples/readme.md#Expressive-Data-Visualization)

There are many reasons for creating Pycharming, but the most important one is that **I hope not only does Pycharming make you love programming for fun or show a magic world to you, but also make this journey relaxing and interesting.**

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/cover.png" alt="cover" width="100%">

## 📎 Links

- [Introduction](./docs/introduction.md)
- [Tutorials](./docs/tutorials/readme.md)
- [API Reference](./docs/api/readme.md)
- [Examples](./docs/examples/readme.md)
- [Processing&P5.js to Pycharming](./docs/processing&p5js-to-charming.md)

## ✨ Features

- **Highly Expressive**: Unlike traditional drawing system or tool using three numerical channels (`(r, g, b)` or `(h, s, v)`) to describe a color, Pycharming allows you to describe a color like `(character, foreground color, background color)`, which means you can express more with the extra the `character` channel.
- **Powerful and Flexible**: Pycharming is not as same as [urwid](https://github.com/urwid/urwid) or [click](https://github.com/pallets/click) to build console line interface. Actually it more like [asciimatics](https://github.com/peterbrittain/asciimatics), [art](https://github.com/sepandhaghighi/art) or [tcharts](https://github.com/ProtoTeam/tcharts.js) to draw some visual effects in the terminal but with more flexibility. Instead of drawing limited and predefined shapes or effects, you can draw some basic primitives, custom shapes, curves, images, typography with transforms (translate, rotate, shear) and even events (mouse, keyboard) in Pycharming.
- **Easy to Learn and Use**: Pycharming is very beginner-friendly, because of Python's simple syntax and [Processing](https://processing.org/)'s concise APIs. It will be more easier if you are already familiar with them. Once you've master Pycharming, you can create anything interesting in you head with it and enjoy the pure joy of coding.

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/hello_world.gif" alt="Charming" width="100%">

## 📦 Installation

- **Supported OS**: Pycharming currently only supports **MacOS**, though it should also work for any other platform that provides a working [curses](https://docs.python.org/3/howto/curses.html) implementation. It soon will support **Windows** and run in **Modern Browsers**.
- **Python**: 3.6/3.7/3.8

```bash
$ pip3 install charming --user
```

## 📺 A Simple Example

```python
'''rect.py'''
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

## 🛸 Future work

- Using Rust as backend to run in browser and support multiple OS, using both JavaScript and Python as frontend.
- Add more API to be more expressive.
- Build a community and online playground like OpenProcessing.

## 💳 License

Pycharming is [LGPL-2.1 License](./LICENSE).
