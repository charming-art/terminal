# Charming: Character Terminal Art Programing

## Overview

Charming is a creative coding language designed for **interactive character terminal art**.

It currently written in Python and provides Processing-like APIs, which aims to help artists, designers, educators, beginners, and anyone else to easily make **ascii art animation**,  **character-style generative art**, **terminal game application** and **expressive data visulization**.

[Documation](./docs/readme.md) | [Examples](./examples) | [Tests Samples](./tests)

## Why is it

### Renaissance of ASCII Art

With [Open Frameworks](https://github.com/openframeworks/openFrameworks), [Processing](https://github.com/processing/processing), [P5js](https://github.com/processing/p5.js) getting more and more popular, people pay more attention on using computer and coding to make exquisite and complex artworks or infomation graphics nowadays. Here are some exmaples created by me.

<a href="https://www.openprocessing.org/sketch/748916"><img src="https://openprocessing-usercontent.s3.amazonaws.com/thumbnails/visualThumbnail748916@2x.jpg" height="192px"></a>
<a href="https://www.openprocessing.org/sketch/757223"><img src="https://openprocessing-usercontent.s3.amazonaws.com/thumbnails/visualThumbnail757223@2x.jpg" height="192px"></a>
<a href="https://www.openprocessing.org/sketch/720376"><img src="https://openprocessing-usercontent.s3.amazonaws.com/thumbnails/visualThumbnail720376@2x.jpg" height="192px"></a>
<a href="https://www.openprocessing.org/sketch/736203"><img src="https://openprocessing-usercontent.s3.amazonaws.com/thumbnails/visualThumbnail736203@2x.jpg" height="192px"></a>

It seems like we gradully forget an old and pure form of art which was born with the computer and programer -- [ASCII Art](https://en.wikipedia.org/wiki/ASCII_art), pictures pieced together from the 95 printable (from a total of 128) characters defined by the ASCII Standard. There are some examples from [textfancy](https://textfancy.com/gallery/).

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/baby.png" height="192px">
<img src="https://raw.githubusercontent.com/charming-art/public-files/master/spiderman.png" height="192px">
<img src="https://raw.githubusercontent.com/charming-art/public-files/master/batman.png" height="192px">

Back in 1970s and early 1980s, computers were not as accessible as now, neverthless to create sophisticated visual effects. But at that time, ASCII Art had showed up and somehow meant to belong to the programmers of that genertion who mostly programmed in a text-based terminal day and night, so ASCII Art may be the best way to show the original charm and romance of computers and of programmers.

So it is tme for us to revive the ASCII Art.

### Powerful and intuitive

Charming is not the first tool which can make ANSCII Art and will certainly not be the last one , but it is more powerful and intuitive than most of exsiting tools.

On the one hand, we are not in 1970s or early 1980s after all, it will be very awkward if we limit ASCII Art to ASCII code and images.

With the appearence of [Unicode](https://en.wikipedia.org/wiki/Unicode) (including [CJK characters](https://en.wikipedia.org/wiki/CJK_characters) and [Emoji](https://en.wikipedia.org/wiki/Emoji)) and the concept of [Generative Art](http://taggedwiki.zubiaga.org/new_content/0a0de87b1c9b14a3530beac00afcbea2), it is time for us to expand the boundaries of ASCII Art to **Character Terminal Art**, which means using characters(not just ASCII characters) and algorithms to create awsome artworks in the terminal.

Charming is born for Character Terminal Art, so only a small part of APIs are related to ASCII Art. Its power focus on drawing some basic shapes such as line, rectangle, circle, bezier curve, etc. or make some transformations including rotate, translate, scale and shear.

On the other hand, being powerful usually means complex usage and steep leanrning curve because of its flexibility.

But thanks to Processing and P5js, they have already introduced a intutive way of coding to the public. Charming makes full use of that and provide similar APIs with them, so you can code in Charming just like code in Processnig or P5js if you are familiar with them.

### Have fun and to be present

With the help of artificial intelligence, computer science and software engineering gain more and more attention and so does Python. A large number of people choose to learn Python to make a living, but programming and Python are far more than that.

Just like most of us do not play basketball for career purpose, we should consider programming or programming in Python as a new kind of hobby. Because life can be without machine learning, web crawler or automated operations, but it can not be without creating and sharing things to have fun and to be present.

I hope not only does Charming make you love programming for fun or show a magic world to you, but also make this journey relaxing and memorable.

## Get started

> Charming currently only supports **MacOS**, though it should also work for any other platform that provides a working [curses](https://docs.python.org/3/howto/curses.html) implementation. It soon will support **Windows** and running in **modern browsers**.

It is very easy to get started with Charming as long as you install [Python3.6+](https://www.python.org/downloads/) already.

First of all, open an terminal and excute the command as below.

```bash
pip3 install charming
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

Finllay, open an terminal and run command as below. Congratulations to you if you get a simple rectangle in your terminal.

```bash
python3 sketch.py
```

![get started](https://raw.githubusercontent.com/charming-art/public-files/master/get_started.png)

## Features

To better show the features of Charming, the following introduction will take Processing as a reference and comparision.

### Structure

Like there are static mode for static effects and active mode for dynamic effects in Processing, you can also use them in Charming but with a little difference.

In Processing, you needn't import APIs or call an extra method to run the sketch, but you need import APIs at first and call a extar method `run` to run the sketch in Charming.

```processing
/* processing code: static mode */

size(300, 200);
rect(0, 0, 100, 150);
```

![processnig structure](https://raw.githubusercontent.com/charming-art/public-files/master/processing_structure_static.png)

```python
''' charming code: static mode '''

# import APIs
import charming as app

app.size(30, 20)
app.rect(0, 0, 10, 10)

# run sketch
app.run()
```

![processnig static structure](https://raw.githubusercontent.com/charming-art/public-files/master/structure_static.png)

Processing will automatically run the `setup` and `draw` functions you defined, but Charming will run them only they have been registered by specific dedecorators.

```processing
/* processing code: active mode */

void setup() {
    size(300, 200);
}

int x = 0;

void draw() {
    background(0);
    x += 1;
    rect(x, 0, 100, 150);
}
```

![processnig activestructure](https://raw.githubusercontent.com/charming-art/public-files/master/processing_structure_active.gif)

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

In Processing, a color normally has three of four channels: `(r, g, b)` or `(r,g, b, a)` in RGB color mode and `(h, s, b)` or `(h, s, b, a)` in HSB mode, each channel is represented by a number.

```processing
/* processing color*/

size(300, 200);
stroke(255, 0, 0);
fill(255, 255, 0);
rect(0, 0, 100, 100);
```

![processnig color](https://raw.githubusercontent.com/charming-art/public-files/master/processing_color.png)

But things are very different in Charming. In Charming, a color consists of three channels: `(ch, fg, bg)`.

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

As a result of the terminal limitation, there are only 256 ANSI colors avilable for terminal which are respresent by 0 ~ 255. Aslo, you can use `RED, BLACK, CYAN, YELLOW, GREEN, BLUE, WHITE, MAGENTA` directly.

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

```py
''' charming: double mode'''

app.size(60, 30, app.DOUBLE)

app.stroke('@', fg=app.GREEN)
app.fill('🚀', bg=app.BLUE)
app.rect(0, 0, 10, 10)

app.run()
```

`CColor` plays a very important role in Charming programs, because compared to normal color, it offer more information which means **it can be less predictable and more meaningful**.

### Typography

It is as easy as Processing to display text in Charming, but only with three level of text size.

- **NORMAL**: draw some basic words or ANSII art to the terminal.
- **BIG**: easily convert some normal words to ANSII art words.
- **LARGE**: convert some ANSII art words to a bigger ANSII art words.

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

In Charming, it is possible for you to draw a image to terminal as simple as Processing, but only a subset of raw pixels will be displayed.

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

Simliar to `setup` and `draw` function, you must regerster event listerner by decorator. Take `mouse_pressed` as an example.

```py
''' charming: event'''

import charming as app

@app.setup
def setup():
    app.size(30, 20)

@app.draw
def draw():
    pass

@app.mouse_pressed
def mouse_pressed():
    pass
```

### Helpers

## Future Works

- **Tests and Bug Fix**: There may be some bugs because Charming have just been simply tested, so one of future works is to test and fix bugs.
- **Improve Performance**: Now both of the frontend and the backgend of Charming are implemented in Python, there's plan to rewrite backend in Rush or C++ and refactor some render algorithms such as polygon filling to achieve a better performance.
- **API Enhancement**: Add more cool APIs accroding to the feature of terminal and character.
- **More Examples**: Write more interesting examples:
  - ascii art animation
  - character-style
  - generative art
  - terminal game
  - expressive data visulization
- **Better Documatation**: Write usages, parameters, returens, examples for each API.
