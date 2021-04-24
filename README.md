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

## Why is it

With [Open Frameworks](https://github.com/openframeworks/openFrameworks), [Processing](https://github.com/processing/processing), [P5js](https://github.com/processing/p5.js) getting more and more popular, people pay more attention on using computer and coding to make exquisite and complex artworks or information graphics nowadays. Here are some examples created by me.

<a href="https://www.openprocessing.org/sketch/748916"><img src="https://openprocessing-usercontent.s3.amazonaws.com/thumbnails/visualThumbnail748916@2x.jpg" height="190px" /></a>&ensp;
<a href="https://www.openprocessing.org/sketch/757223"><img src="https://openprocessing-usercontent.s3.amazonaws.com/thumbnails/visualThumbnail757223@2x.jpg" height="190px" /></a>&ensp;
<a href="https://www.openprocessing.org/sketch/720376"><img src="https://openprocessing-usercontent.s3.amazonaws.com/thumbnails/visualThumbnail720376@2x.jpg" height="190px" /></a>&ensp;
<a href="https://www.openprocessing.org/sketch/736203"><img src="https://openprocessing-usercontent.s3.amazonaws.com/thumbnails/visualThumbnail736203@2x.jpg" height="190px" /></a>

In this case, why we need a new creative coding language?

### Renaissance of ASCII Art

First of all, it seems like we gradually forget an old and pure form of art which was born with the computer and programmer -- [ASCII Art](https://en.wikipedia.org/wiki/ASCII_art), pictures pieced together from the 95 printable (from a total of 128) characters defined by the ASCII Standard. There are some examples from [textfancy](https://textfancy.com/gallery/).

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/baby.png" height="192px" />&emsp;<img src="https://raw.githubusercontent.com/charming-art/public-files/master/spiderman.png" height="192px" />&emsp;<img src="https://raw.githubusercontent.com/charming-art/public-files/master/batman.png" height="192px" />

Back in 1970s and early 1980s, computers were not as accessible as now, nevertheless to create sophisticated visual effects. But at that time, ASCII Art had showed up and somehow meant to belong to the programmers of that generation who mostly programmed in a text-based terminal day and night, so **ASCII Art may be the best way to show the original charm and romance of computers and of programmers.**

For example, it will be very romantic if you using snake-eating to write a poem. Here is an example created by Charming that you move the snake, eat the food and finally you get the poem: [This Is Just To Say](https://www.poetryfoundation.org/poems/56159/this-is-just-to-say).

<a href="https://github.com/charming-art/charming/blob/master/examples/snake.py"><img src="https://raw.githubusercontent.com/charming-art/public-files/master/snake.gif" /></a>

So we have to make the ASCII Art prosperous again.

### Powerful and intuitive

Then, Charming is not the first tool which can make ANSCII Art and will certainly not be the last one , but it is more powerful and intuitive than most of existing tools.

We are not in 1970s or early 1980s after all, it will be very awkward if we limit ASCII Art to ASCII code and images.

With the appearance of [Unicode](https://en.wikipedia.org/wiki/Unicode) (including [CJK characters](https://en.wikipedia.org/wiki/CJK_characters) and [Emoji](https://en.wikipedia.org/wiki/Emoji)) and the concept of [Generative Art](http://taggedwiki.zubiaga.org/new_content/0a0de87b1c9b14a3530beac00afcbea2), it is time for us to expand the boundaries of ASCII Art to **Character Terminal Art**, which means using characters(not just ASCII characters) and algorithms to create awesome artworks in the terminal.

The biggest benefit of using characters is that we can encoding more information for our artworks besides color, which means we can easily express more than traditional styles.

Take data visualization as a example. A common belief for data visualization is that visual representations should maximize the data-ink ratio and avoid unnecessary decoration as much as possible, and colors do a great job on it.

But if we extend the concept of color to include character, the character definitely can give extra information which will give the data visualization **memorability**, **aesthetics**, and **engagement** Recently, researchers have started exploring them, and these metrics focus on communication and presentation rather than data exploration and analysis.

<a href="https://github.com/charming-art/charming/blob/master/examples/barchart.py"><img src="https://raw.githubusercontent.com/charming-art/public-files/master/barchart.png" /></a>

There is a bar chart for mock data about covid-19 virus created by Charming. Instead of only using green for the curve, red for the confirm, gray for the dead, it also use 🌈 to express happiness and hopefulness, use 🦠 to strengthen the warning, and use ☠️ to show sadness and fear. They are indeed make this chart more vivid and unforgettable.

Charming is born for Character Terminal Art, so only a small part of APIs are related to ASCII Art. Its power focus more on drawing some basic shapes such as *line*, *rectangle*, *circle*, *bezier curve*, *custom shape*, etc. or apply some transformations including *rotate*, *translate*, *scale* and *shear*.

<a href="https://github.com/charming-art/charming/blob/master/tests/test_shape_primitives.py"><img src="https://raw.githubusercontent.com/charming-art/public-files/master/primitives.png" height="150px" /></a>&emsp;<a href="https://github.com/charming-art/charming/blob/master/tests/test_transform.py"><img src="https://raw.githubusercontent.com/charming-art/public-files/master/transforms.png" height="150px" /></a>&emsp;<a href="https://github.com/charming-art/charming/blob/master/tests/test_shape_vertex.py" ><img src="https://raw.githubusercontent.com/charming-art/public-files/master/vertex.png" height="150px" /></a>

### Easy to learn and use

Being powerful usually means complex usage and steep learning curve because of its flexibility.

But thanks to Processing and P5js, they have already introduced a intuitive way of coding to the public. Charming makes full use of that and provide similar APIs with them, so you can code in Charming just like code in Processing or P5js if you are familiar with them.

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/code1.png" height="300px" />&emsp;<img src="https://raw.githubusercontent.com/charming-art/public-files/master/code2.png" height="300px" />

### Have fun and to be present

Last but not the least, I hope not only does Charming make you love programming for fun or show a magic world to you, but also make this journey relaxing and interesting.

With the help of artificial intelligence, computer science and software engineering gaining more and more attention and so does Python, a large number of people choose to learn Python to make a living, but programming and Python are far more than that.

Just like most of us do not play basketball for career purpose, we should consider programming or programming in Python as a new kind of hobby. Because life can be without machine learning, web crawler or automated operations, but it can not be without creating and sharing things to have fun and to be present.

**With the help of Charming, you are able to print something really awesome at the terminal when you are learning Python instead of just print some boring and stupid log information.**

![charm](https://raw.githubusercontent.com/charming-art/public-files/master/charm.png)

## Tutorials

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
