# Charming: Character Terminal Art Programing

- [Charming: Character Terminal Art Programing](#charming-character-terminal-art-programing)
  - [Overview](#overview)
  - [Why is it](#why-is-it)
    - [Renaissance of ASCII Art](#renaissance-of-ascii-art)
    - [Powerful and intuitive](#powerful-and-intuitive)
    - [Have fun and to be present](#have-fun-and-to-be-present)
  - [Get started](#get-started)
  - [Features](#features)
    - [Structure](#structure)
      - [Static Mode](#static-mode)
      - [Active Mode](#active-mode)
    - [Color](#color)
      - [Basic Use](#basic-use)
      - [RGB Color Mode](#rgb-color-mode)
      - [HSB Color Mode](#hsb-color-mode)
      - [Double mode](#double-mode)
    - [Typography](#typography)
      - [Normal Size](#normal-size)
      - [Big Size](#big-size)
      - [Large Size](#large-size)
    - [Image](#image)
    - [Events](#events)
    - [Helpers](#helpers)
  - [Future Works](#future-works)

## Overview

Charming is a creative coding language designed for **interactive character terminal art**.

It currently written in Python and provides Processing-like APIs, which aims to help artists, designers, educators, beginners, and anyone else to easily create **ascii art animation**,  **character-style generative art**, **terminal game application** and **expressive data visualization**.

Generally speaking, Charming allows you write simple code like this.

```py
import charming as app

x = 0


@app.setup
def setup():
    app.full_screen()
    app.no_cursor()
    app.stroke('@', app.YELLOW, app.RED)
    app.fill('+', app.GREEN, app.BLUE)


@app.draw
def draw():
    global x
    app.background(' ')
    app.rect(x, 0, 10, 10)
    x += 1


app.run()
```

And you will get this in your local terminal.

![welcome](https://raw.githubusercontent.com/charming-art/public-files/master/welcome.gif)

[Documentation](./docs/readme.md) | [Examples](./examples) | [Tests Samples](./tests)

<a href="./examples/heart.py"><img src="https://raw.githubusercontent.com/charming-art/public-files/master/example_heart.gif" height="192px" ></a>&emsp;<a href="./examples/barchart.py"><img src="https://raw.githubusercontent.com/charming-art/public-files/master/example_barchart.png" height="192px" ></a>&emsp;<a href="./examples/snake.py"><img src="https://raw.githubusercontent.com/charming-art/public-files/master/example_snake.gif" height="192px"></a>

## Why is it

### Renaissance of ASCII Art

With [Open Frameworks](https://github.com/openframeworks/openFrameworks), [Processing](https://github.com/processing/processing), [P5js](https://github.com/processing/p5.js) getting more and more popular, people pay more attention on using computer and coding to make exquisite and complex artworks or information graphics nowadays. Here are some examples created by me.

<a href="https://www.openprocessing.org/sketch/748916"><img src="https://openprocessing-usercontent.s3.amazonaws.com/thumbnails/visualThumbnail748916@2x.jpg" height="192px"></a>
<a href="https://www.openprocessing.org/sketch/757223"><img src="https://openprocessing-usercontent.s3.amazonaws.com/thumbnails/visualThumbnail757223@2x.jpg" height="192px"></a>
<a href="https://www.openprocessing.org/sketch/720376"><img src="https://openprocessing-usercontent.s3.amazonaws.com/thumbnails/visualThumbnail720376@2x.jpg" height="192px"></a>
<a href="https://www.openprocessing.org/sketch/736203"><img src="https://openprocessing-usercontent.s3.amazonaws.com/thumbnails/visualThumbnail736203@2x.jpg" height="192px"></a>

It seems like we gradually forget an old and pure form of art which was born with the computer and programmer -- [ASCII Art](https://en.wikipedia.org/wiki/ASCII_art), pictures pieced together from the 95 printable (from a total of 128) characters defined by the ASCII Standard. There are some examples from [textfancy](https://textfancy.com/gallery/).

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/baby.png" height="192px" >&emsp;<img src="https://raw.githubusercontent.com/charming-art/public-files/master/spiderman.png" height="192px" >&emsp;<img src="https://raw.githubusercontent.com/charming-art/public-files/master/batman.png" height="192px">

Back in 1970s and early 1980s, computers were not as accessible as now, nevertheless to create sophisticated visual effects. But at that time, ASCII Art had showed up and somehow meant to belong to the programmers of that generation who mostly programmed in a text-based terminal day and night, so **ASCII Art may be the best way to show the original charm and romance of computers and of programmers.**

For example, it will be very romantic if you using snake-eating to write a poem. Here is an example created by Charming that you move the snake, eat the food and finally you get the poem: [This Is Just To Say](https://www.poetryfoundation.org/poems/56159/this-is-just-to-say).

<a href="./examples/snake.py">![charm](https://raw.githubusercontent.com/charming-art/public-files/master/snake.gif)</a>

So we have to make the ASCII Art prosperous again.

### Powerful and intuitive

Charming is not the first tool which can make ANSCII Art and will certainly not be the last one , but it is more powerful and intuitive than most of existing tools.

On the one hand, we are not in 1970s or early 1980s after all, it will be very awkward if we limit ASCII Art to ASCII code and images.

With the appearance of [Unicode](https://en.wikipedia.org/wiki/Unicode) (including [CJK characters](https://en.wikipedia.org/wiki/CJK_characters) and [Emoji](https://en.wikipedia.org/wiki/Emoji)) and the concept of [Generative Art](http://taggedwiki.zubiaga.org/new_content/0a0de87b1c9b14a3530beac00afcbea2), it is time for us to expand the boundaries of ASCII Art to **Character Terminal Art**, which means using characters(not just ASCII characters) and algorithms to create awesome artworks in the terminal.

**The biggest benefit of using characters is that we can encoding more information for our artworks besides color, which means we can easily express more than traditional styles.**

Take data visualization as a example. A common belief for data visualization is that visual representations should maximize the data-ink ratio and avoid unnecessary decoration as much as possible, and colors do a great job on it.

But if we extend the concept of color to include character, the character definitely can give extra information which will give the data visualization **memorability**, **aesthetics**, and **engagement** Recently, researchers have started exploring them, and these metrics focus on communication and presentation rather than data exploration and analysis.

There is a bar chart for mock data about covid-19 virus created by Charming. Instead of only using green for the curve, red for the confirm, gray for the dead, it also use 🌈 to express happiness and hopefulness, use 🦠 to strengthen the warning, and use ☠️ to show sadness and fear. They are indeed make this chart more vivid and unforgettable.

<a href="./examples/barchart.py">![charm](https://raw.githubusercontent.com/charming-art/public-files/master/barchart.png)</a>

Charming is born for Character Terminal Art, so only a small part of APIs are related to ASCII Art. Its power focus more on drawing some basic shapes such as *line*, *rectangle*, *circle*, *bezier curve*, *custom shape*, etc. or apply some transformations including *rotate*, *translate*, *scale* and *shear*.

<a href="./tests/test_shape_primitives.py"><img src="https://raw.githubusercontent.com/charming-art/public-files/master/primitives.png" height="165px" ></a>&emsp;<a href="./tests/test_transform.py"><img src="https://raw.githubusercontent.com/charming-art/public-files/master/transforms.png" height="165px" ></a>&emsp;<a href="./tests/test_shape_vertex.py"><img src="https://raw.githubusercontent.com/charming-art/public-files/master/vertex.png" height="165px"></a>

On the other hand, being powerful usually means complex usage and steep learning curve because of its flexibility.

But thanks to Processing and P5js, they have already introduced a intuitive way of coding to the public. Charming makes full use of that and provide similar APIs with them, so you can code in Charming just like code in Processing or P5js if you are familiar with them.

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/code1.png" height="250px" >&emsp;<img src="https://raw.githubusercontent.com/charming-art/public-files/master/code2.png" height="250px" >

### Have fun and to be present

With the help of artificial intelligence, computer science and software engineering gaining more and more attention and so does Python, a large number of people choose to learn Python to make a living, but programming and Python are far more than that.

Just like most of us do not play basketball for career purpose, we should consider programming or programming in Python as a new kind of hobby. Because life can be without machine learning, web crawler or automated operations, but it can not be without creating and sharing things to have fun and to be present.

**With the help of Charming, you are able to print something really awesome at the terminal when you are learning Python instead of just print some boring and stupid log information.**

In that case, I hope not only does Charming make you love programming for fun or show a magic world to you, but also make this journey relaxing and interesting.

![charm](https://raw.githubusercontent.com/charming-art/public-files/master/charm.png)

## Get started

> Charming currently only supports **MacOS**, though it should also work for any other platform that provides a working [curses](https://docs.python.org/3/howto/curses.html) implementation. It soon will support **Windows** and run in **modern browsers**.

It is very easy to get started with Charming as long as you install [Python3.6+](https://www.python.org/downloads/) already.

First of all, open a terminal and execute the command as below.

```bash
pip3 install charming --user
```

Then, create a file named `sketch.py` and copy the code to it and save.

```py
''' sketch.py '''

import charming as app

# draw a rect
app.full_screen()
app.rect(0, 0, 10, 10)

# run the sketch
app.run()
```

Finally, open a terminal and run command as below. Congratulations to you if you get a simple rectangle in your terminal.

```bash
python3 sketch.py
```

![get started](https://raw.githubusercontent.com/charming-art/public-files/master/get_started.png)

## Features

To better show the features of Charming, the following introduction will take Processing as a reference and comparison.

### Structure

Like there are static mode for static effects and active mode for dynamic effects in Processing, you can also use them in Charming but with a little difference.

#### Static Mode

In Processing, you needn't import APIs or call an extra method to run the sketch, but you need import APIs at first and call an extra method `run` to run the sketch in Charming.

```processing
/* processing code: static mode */

size(900, 300);
rect(0, 0, 100, 150);
```

![processnig structure](https://raw.githubusercontent.com/charming-art/public-files/master/processing_structure_static.png)

```python
''' charming code: static mode '''

# import APIs
import charming as app

app.full_screen()
app.rect(0, 0, 10, 10)

# run sketch
app.run()
```

![processnig static structure](https://raw.githubusercontent.com/charming-art/public-files/master/structure_static.png)

#### Active Mode

Processing will automatically run the `setup` and `draw` functions you defined, but Charming will run them only they have been registered by specific decorators.

```processing
/* processing code: active mode */

void setup() {
    size(900, 300);
}

int x = 0;

void draw() {
    background(0);
    x += 1;
    rect(x, 0, 100, 150);
}
```

![processnig active structure](https://raw.githubusercontent.com/charming-art/public-files/master/processing_structure_active.gif)

```py
''' charming code: active mode '''

import charming as app

@app.setup
def setup():
    app.full_screen()

x = 0

@app.draw
def draw():
    app.background(' ')
    global x
    x += 1
    app.rect(x, 0, 10, 10)

app.run()
```

![active structure](https://raw.githubusercontent.com/charming-art/public-files/master/structure_active.gif)

### Color

The biggest difference between Charming or Processing is the definition of color, which make Charming so unique to some extend.

In Processing, a color normally has three or four channels: `(r, g, b)` or `(r,g, b, a)` in RGB color mode and `(h, s, b)` or `(h, s, b, a)` in HSB mode, each channel is represented by a number.

```processing
/* processing color*/

size(900, 300);
stroke(255, 0, 0);
fill(255, 255, 0);
rect(0, 0, 100, 100);
```

![processnig color](https://raw.githubusercontent.com/charming-art/public-files/master/processing_color.png)

#### Basic Use

Colors are very different in Charming. In Charming, a color consists of three channels: `(ch, fg, bg)`.

- `ch`: character, ascii code or unicode (including cjk characters or emoji).
- `fg`: foreground color, a number(0 ~ 255 by default) if the color mode is ANSI, a tuple with length equaling to 1or 3 if the color mode is HSB or RGB.
- `bg`: background color, a number(0 ~ 255 by default) if the color mode is ANSI, a tuple with length equaling to 1 or 3 if the color mode is HSB or RGB.

```py
''' charming color: ANSI '''

import charming as app

app.full_screen()
app.no_cursor()
app.stroke('O', app.GREEN, app.MAGENTA)
app.fill('X', 93, 220)
app.rect(0, 0, 10, 10)

app.run()
```

![ansi color](https://raw.githubusercontent.com/charming-art/public-files/master/color.png)

#### RGB Color Mode

As a result of the terminal limitation, there are only 256 ANSI colors available for terminal which are represent by 0 ~ 255. Also, you can use `RED, BLACK, CYAN, YELLOW, GREEN, BLUE, WHITE, MAGENTA` directly.

But in Charming, you can still use a tuple to represent the `fg` and `bg` of a color if you change the color mode to RGB or HSB, and they are convert to the closet color among the ANSI colors.

```py
''' charming color: RBG '''

import charming as app

# Set color mode to RGB
app.color_mode(app.RGB)
app.no_cursor()
app.full_screen()

for i in range(7):
    v = app.map(i, 0, 7, 0, 255)
    app.stroke_weight(1)

    # r
    app.stroke('@', (v, 0, 0), (v, 0, 0))
    app.point(i * 4, 5)

    # g
    app.stroke('@', (0, v, 0), (0, v, 0))
    app.point(i * 4, 10)

    # b
    app.stroke('@', (0, 0, v), (0, 0, v))
    app.point(i * 4, 15)

app.run()
```

![rgb color](https://raw.githubusercontent.com/charming-art/public-files/master/rgb_color.png)

#### HSB Color Mode

```py
''' charming color: HSB '''

import charming as app

# Set color mode to HSB
app.color_mode(app.HSB)
app.full_screen()
app.no_cursor()

for h in range(360):
    x = h % 30
    y = h // 30
    app.stroke('@', (h, 100, 100), (h, 100, 100))
    app.point(x, y)

app.run()
```

![hsb color](https://raw.githubusercontent.com/charming-art/public-files/master/hsb_color.png)

#### Double mode

You may already found something not work as expected.

- Squares and ellipses drawn on the terminal are deformative.
- Color with unicode character cause some confusing result.

The first one is that each cell of the terminal are not square which means that its width doesn't equal to its height. And the second one is that normally ascii codes need one cell to display and unicodes need two cell to display.

In order to solve both of them, you can change the renderer of Charming to `DOUBLE` mode when you call `size()` or `full_screen()`. In that mode, Charming will use two cells to display both of ascii codes and unicodes.

```py
''' charming: double mode'''
import charming as app

app.full_screen(app.DOUBLE)

app.stroke('@', fg=app.GREEN)
app.fill('🚀', bg=app.BLUE)
app.square(0, 0, 10)

app.fill('0', bg=app.BLUE)
app.circle(20, 10, 10)
app.run()
```

![double mode](https://raw.githubusercontent.com/charming-art/public-files/master/double_mode.png)

There is something important you should pay attention to. **Charming can't always get the right width of unicodes, so if you find something wrong when using unicodes, you can declare the width of that unicode directly.**

```py
''' charming: double mode'''

app.full_screen(app.DOUBLE)

app.stroke('@', fg=app.GREEN)

# use a tuple to declare the width of that unicode
app.fill(('⏰', 2), bg=app.BLUE)
app.square(0, 0, 10)

app.run()
```

### Typography

It is as easy as Processing to display text in Charming, but only with three level of text size.

- **NORMAL**: Draw some basic words or ANSII Art to the terminal.
- **BIG**: Easily convert some normal words to ANSII Art words.
- **LARGE**: Convert some ANSII Art words to a bigger ANSII Art words.

#### Normal Size

```py
''' charming text: normal size '''

import charming as app

app.full_screen()

head = r'''
         .-"""-.
        /       \
        \       /
 .-"""-.-`.-.-.<  _
/      _,-\ ()()_/:)
\     / ,  `     `|
 '-..-| \-.,___,  /
       \ `-.__/  /
        `-.__.-'`
'''

# draw basic texts
app.text('charming', 0, 0)

# draw some ascii art
app.text(head, 0, 5)

app.run()
```

![normal text](https://raw.githubusercontent.com/charming-art/public-files/master/text_normal.png)

#### Big Size

```py
''' charming text: big size '''

import charming as app

app.full_screen()

# convert basic text to ascii text
app.text_size(app.BIG)
app.text('charming', 0, 0)

# support many fonts
fonts = app.get_font_list()
app.text_font(fonts[2])
app.text('charming', 0, 10)

app.run()
```

![big text](https://raw.githubusercontent.com/charming-art/public-files/master/big_text.png)

#### Large Size

```py
''' charming text: normal size '''

import charming as app

app.full_screen()
app.no_cursor()

head = r'''
         .-"""-.
        /       \
        \       /
 .-"""-.-`.-.-.<  _
/      _,-\ ()()_/:)
\     / ,  `     `|
 '-..-| \-.,___,  /
       \ `-.__/  /
        `-.__.-'`
'''

# convert ascii text to a lager ascii text
app.text_size(app.LARGE)
app.text(head, 0, 0)

app.run()
```

![large text](https://raw.githubusercontent.com/charming-art/public-files/master/text_large.png)

### Image

In Charming, it is possible for you to draw an image to terminal as simple as Processing, but only a subset of raw pixels will be displayed.

```py
''' charming: image '''

import charming as app

app.no_cursor()
app.full_screen()
img = app.load_image('avatar.png')
app.image(img, 0, 0, 60, 30)

app.run()
```

![image](https://raw.githubusercontent.com/charming-art/public-files/master/image.png)

### Events

Events means you can bring life to your artworks, because you can interact with it and it will give you feedback.

Similar to `setup` and `draw` function, you must register event listeners (`mouse_pressed`, `key_pressed`, etc.) by decorators.

Besides mouse events and keyboard events, Charming provide a unique type of events which deeply embed in terminal: **cursor events**, which will be triggered if you type or press the `UP/Right/DOWN/LEFT` arrow keys to move the cursor on the terminal.

```py
''' charming: event'''

import charming as app

@app.setup
def setup():
    app.full_screen()
    app.color_mode(app.RGB)
    width = app.get_width()
    height = app.get_height()

    # set the cursor at the middle of the screen
    # and hide it
    app.set_cursor(width / 2, height / 2)
    app.no_cursor()

points = []

@app.draw
def draw():
    app.background(' ')
    for i, p in enumerate(points):
        c = app.map(i, 0, len(points), 0, 255)
        app.stroke('@', (c, 0, 0), (c, c, 0))
        app.point(p.x, p.y)

@app.cursor_pressed
def cursor_pressed():
    # add a point if cursor moved
    x = app.get_cursor_x()
    y = app.get_cursor_y()
    points.append(app.CVector(x, y))

app.run()
```

![image](https://raw.githubusercontent.com/charming-art/public-files/master/cursor_event.gif)

### Helpers

Because Charming use the terminal as the canvas to paint, so it is impossible for you to print some information to the console. Instead you can use the `print` function from Charming to print some information to file named `charming.log`.

```py
import charming as app

n = 1
s = 'hello'
d = {
    'name': 'charming',
    'awesome': True
}
t = (1, 2)

app.print(n, s, d, key=t)
```

```plain text
# charming.log

DEBUG:root:123, ['h', 2], {'name': 'charming', 'awesome': True}, {'key': (0, 1)}
```

## Future Works

- **More accessible**: As soon as Charming can run in modern browsers, there will be a online playground to try it online and may be a platform to create, sharing Charming sketches with others like [OpenProcessing](https://www.openprocessing.org/).
- **Tests and Bug Fix**: There may be some bugs because Charming have just been simply tested, so one of future works is to test and fix bugs.
- **Improve Performance**: Now both of the frontend and the backend of Charming are implemented in Python, there's a plan to rewrite backend in Rust or C++ and refactor some rendering algorithms such as polygon filling to achieve a better performance.
- **API Enhancement**: Add more cool APIs according to the feature of terminal and character.
- **More Examples**: Write more interesting examples.
  - ascii art animation
  - character-style generative art
  - terminal game
  - expressive data visualization
- **Better Documentation**: Write usages, parameters, returns, examples for each API.
