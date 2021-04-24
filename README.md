# Charming

Charming is a creative coding language designed for **Character Terminal Art Programming**.

It currently written in Python and provides Processing-like APIs, which aims to help artists, designers, educators, beginners, and anyone else to easily create:

- ASCII Art Animation
- Character-Style Generative Art
- Terminal Game Application
- Expressive Data Visualization

<a href="https://charming-art.github.io/"><img src="https://raw.githubusercontent.com/charming-art/public-files/master/home_code.png" alt="Charming" height="320"></a>&ensp;
<a href="https://charming-art.github.io/"><img src="https://raw.githubusercontent.com/charming-art/public-files/master/welcome.gif" alt="Charming" height="320"></a>

## Installation

- **Supported OS**: Charming currently only supports **MacOS**, though it should also work for any other platform that provides a working [curses](https://docs.python.org/3/howto/curses.html) implementation. It soon will support **Windows** and run in **Modern Browsers**.
- **Python**: 3.6/3.7/3.8

```bash
pip3 install charming --user
```

## A Simple Example

```py
# save this as sketch.py
import charming as app

# draw a rect
app.full_screen()
app.rect(0, 0, 10, 10)

# run the sketch
app.run()
```

```py
python3 sketch.py
```

![get started](https://raw.githubusercontent.com/charming-art/public-files/master/get_started.png)

## Gallery

|  [Heart](./examples/heart/readme.md)   |  [Covid Bar Chart](./examples/barchart/readmd.md) |  [Eating Poetry](./examples/snake/readme.md) | [More](./docs/gallery.md) |
|  :--:  |  :--: | :--:  | :--: |
| <img src="https://raw.githubusercontent.com/charming-art/public-files/master/example_heart.gif" height="180px" alt="heart" />|<img src="https://raw.githubusercontent.com/charming-art/public-files/master/example_barchart.png" height="180px" alt="bar chart" />|<img src="https://raw.githubusercontent.com/charming-art/public-files/master/example_snake.gif" alt="snake" height="180px" /> | 👀 |

## Tutorials

- [Why is it](./docs/tutorials/why-is-it.md)
- [Structure](./docs/tutorials/stucture.md)
- [Color](./docs/tutorials/color.md)
- [Shape](./docs/tutorials/shape.md)
- [Image](./docs/tutorials/image.md)
- [Typography](./docs/tutorials/typography.md)
- [Event](./docs/tutorials/event.md)
- [Helper](./docs/tutorials/helper.md)
- [Processing to Charming](./docs/tutorials/processing-to-charming.md)

## API

Charming implements most of Processing's APIs related to 2D, all of the supported APIs are list below. You can take [Processing Documentation](https://processing.org/reference/) as a reference, and take a look at some basic [test samples](https://github.com/charming-art/charming/blob/master/tests/) to be familiar with the supported APIs.

- [Color](./docs/api/color.md)
- [Constant](./docs/api/constant.md)
- [Environment](./docs/api/environment.md)
- [Event](./docs/api/event.md)
- [Helper](./docs/api/helper.md)
- [Image](./docs/api/image.md)
- [Math](./docs/api/math.md)
- [Shape](./docs/api/shape.md)
- [Structure](./docs/api/structure.md)
- [Time](./docs/api/time.md)
- [Transform](./docs/api/transform.md)
- [Typography](./docs/api/typography.md)

## Future Work

- **More accessible**: As soon as Charming can run in modern browsers, there will be a online playground to try it online and may be a platform to create, sharing Charming sketches with others like [OpenProcessing](https://www.openprocessing.org/).
- **Tests and Bug Fix**: There may be some bugs because Charming have just been simply tested, so one of future works is to test and fix bugs.
- **Improve Performance**: Now both of the frontend and the backend of Charming are implemented in Python, there's a plan to rewrite backend in Rust or C++ and refactor some rendering algorithms such as polygon filling to achieve a better performance.
- **API Enhancement**: Add more cool APIs according to the feature of terminal and character.
- **More Examples**: Write more interesting examples：
  - ascii art animation
  - character-style generative art
  - terminal game
  - expressive data visualization
- **Better Documentation**: Write usages, parameters, returns, examples for each API.
  
## License

[LGPL-2.1 License](https://github.com/charming-art/charming/blob/master/LICENSE)
