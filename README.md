# Charming: Character Terminal Art Programing

## Overview

Charming is a creative coding language designed for **interactive terminal art**.

It deeply embedded in Python and provides Processing-like APIs, which aims at help artists, designers, educators, beginners, and anyone else to make **ascii art animation**,  **character-style generative art**, **terminal game** and **expressive data visulization**.

[Documation](./docs/readme.md) | [Examples](./examples) | [Tests](./tests)

## Why is it

### Renaissance of ASCII Art

With [Open Frameworks](https://github.com/openframeworks/openFrameworks), [Processing](https://github.com/processing/processing), [P5js](https://github.com/processing/p5.js) getting more and more popular, people pay more attention on using computer and coding to make exquisite and complex artworks or infomation graphics.

It seems like we gradully forget an old and pure form of art which was born with the computer and programers: [ASCII Art](https://en.wikipedia.org/wiki/ASCII_art), pictures pieced together from the 95 printable (from a total of 128) characters defined by the ASCII Standard.

Back in 1970s and early 1980s, computers were not as accessible as now, neverthless to create sophisticated visual effects. But at that time, ASCII Art had showed up and somehow meant to belong to the programmers of that genertion who mostly programmed in a text-based terminal day and night, so I ASCII Art may be the best way to show the original charm and romance of computers and of programmers.

### Powerful and intuitive

Charming is not the first tool which can make ANSCII Art and will not be the last one for sure, but it is more powerful and intuitive than most of exsiting tools.

On the one hand, we are not in 1970s or early 1980s after all, it will be very ridiculous if we limit ASCII Art to ASCII code and images.

With the apperance of [Unicode](https://en.wikipedia.org/wiki/Unicode) (including [CJK characters](https://en.wikipedia.org/wiki/CJK_characters) and [Emoji](https://en.wikipedia.org/wiki/Emoji)) and the concept of generative art, it is time for us to expand the boundaries of ASCII Art to **Character Terminal Art**, which means using characters(not just ASCII characters) and algorithms to create awsome artworks in the terminal.

Charming is born for Character Terminal Art, so only a small part of APIs are related to ASCII Art. Its power focus more on drawing some basic shapes such as line, rectangle, circle, bezier curve, etc. or make some transformations including rotate, translate, scale and shear.

On the other hand, being powerful usually means complex usage and steep leanrning curve because of its flexibility.

But thanks to Processing and P5js, they have already introduced a intutive way of coding to the public. Charming makes full use of that and provide similar APIs with them, so you can code in Charming just like code in Processnig or P5js if you are familiar with them.

### Have fun and to be present

With the help of artificial intelligence, computer science and software engineering gain more and more attention and so does Python. A large number of people choose to learn Python to make a living, but programming and Python are far more than that.

Just like most of us do not play basketball for career purpose, we should consider programming or programming in Python as a new kind of hobby. Because life can be without machine learning, web crawler or automated operations, but it can not be without creating and sharing things to have fun and to be present.

I hope not only does Charming make you love programming for fun or show a magic world to you, but also make this journey relaxing and memorable.

## Get started

> Charming Currently only supports **MacOS**, though it should also work for any other platform that provides a working [curses](https://docs.python.org/3/howto/curses.html) implementation. It soon will support **Windows** and running in **modern browsers**.

It is very easy to get started with Charming as long as you install [Python3.6+](https://www.python.org/downloads/) already.

First of all, open an terminal and excute command as below.

```bash
pip3 install charming
```

Then, create a file named `sketch.py` and copy the below code to it and save.

```py
# sketch.py
import charming as app

# draw a square
app.full_screen()
app.square(0, 0, 10)

# run the sketch
app.run()
```

Finllay, open an terminal and excute command as below. Congratulations to you if you get a simple square in your terminal.

```bash
python3 sketch.py
```

## Features

To better show the features of Charming, I will take Processing as a reference.

### Structure

Like there are static mode for static effects and active mode for dynamic effects in Processing, you can choose them in Charming but with a little difference.

In Processing, you needn't import APIs or call a extra method to run the sketch, but you need import APIs at first and call a extar method `run` to run the sketch.

```processing
/* processing code: static mode */

size(30, 20);
rect(0, 0, 10, 15);
```

```python
''' charming code: static mode '''

import charming as app # import APIs

app.size(30, 20)
app.rect(0, 0, 10, 15)

app.run() # run sketch
```

Processing will automatically run the `setup` and `draw` functions you defined, but Charming will run them only they have been registered by specific dedecorators.

```processing
/* processing code: active mode */

void setup() {
    size(30, 20);
}

x = 0;

void draw() {
    x += 1;
    rect(x, 0, 10, 15)
}
```

```py
''' charming code: active mode '''

import charming as app

@app.setup
def setup():
    app.size(30, 20)

x = 0

@app.draw
def draw():
    global x
    x += 1
    app.rect(x, 0, 10, 15)

app.run()
```

### CColor

The biggest difference between Charming or Processing is the definition of color, which make Charming so unique in some extend.

In Processing, a color normally has three of four channels: `(r, g, b)` or `(r,g, b, a)` in RGB color mode and `(h, s, b)` or `(h, s, b, a)` in HSB mode, each channel is represented by a number.

```processing
/* processing color*/

size(30, 20);
stroke(255, 0, 0);
fill(255, 255, 0);
rect(0, 0, 10, 15);
```

But things are very different in Charming. In Charming, a color consists of three channels: `(ch, fg, bg)`.

- **ch**: the character which will displayed in terminal cell. It can be any printable characters.
- **fg**: the foreground color of the terminal cell. It should be number from 0 to 255 by default.
- **bg**: the background color of the terminal cell. It should be number from 0 to 255 by default.

```py
''' charming color: ANSI '''

import charming as app

app.size(30, 20);
app.stroke('@', app.RED, app.YELLOW);
app.fill('+', 123, 210);
app.rect(0, 0, 10, 15);

app.run()
```

As a result of the terminal limitation, there are only 256 ANSI colors avilable for terminal which are respresent by 0 ~ 25. Aslo, you can use `RED, BLACK, CYAN, YELLOW, GREEN, BLUE, WHITE, MAGENTA` directly.

Anyway, you can still use a tuple to represent the `fg` and `bg` of a color if you change the color mode to RGB or HSB, and they are convert to the closet color among the ANSI colors.

```py
''' charming color: RBG '''

import charming as app

app.size(30, 20)

for i in range(7):
    r = app.map(i, 0, 7, 0, 255)
    app.stroke('@', (r, 0, 0), (r, 0, 0))
    app.point(i, 0)

app.run()
```

```py
''' charming color: HSB '''

import charming as app

app.size(30, 20)

for i in range(7):
    h = app.map(i, 0, 7, 0, 360)
    app.stroke('@', (h, 100, 100), (h, 100, 100))
    app.point(i, 0)

app.run()
```

There is a problem if you unicode character

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

With the help of normal size text, you can easily draw some basic words or ANSII art to the terminal.

```py
''' charming text: normal size '''

import charming as app

app.size(30, 20)
app.text('charming', 0, 0)
app.run()
```

With the help of big size text, you can easily convert some normal words to ANSII art words.

```py
''' charming text: big size '''

import charming as app

app.size(30, 20)
app.text_size(app.BIG)
app.text('charming', 0, 0)
app.run()
```

With the help of large size text, you can easily convert some ANSII art words to a bigger ANSII art words.

``` py
''' charming text: large size '''

import charming as app

app.size(30, 20)
app.text_size(app.LARGE)
app.text('charming', 0, 0)
app.run()
```

### Image

In Charming, You can draw a image to terminal as simple as Processing, but only a subset of raw pixels will be displayed.

```py
''' charming: image '''
import charming as app

img = app.load_image('avatar.png')
app.size(30, 30)
app.image(img, 0, 0, 30, 30)
app.run()
```

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

#### Mouse

- mouse_pressed()
- mouse_relesed()
- mouse_clicked()
  
#### Keyboard

- key_pressed()
- key_typed()
- key_released()

#### Cursor

- cursor_moved()

### Helpers

## Future Works

- **Tests and Bugfix**: There may be some bugs exsist because Charming have just been simple tested, so one of future works is to test and fix bugs.
- **Improve Performance**: Now both of the frontend and the backgend of Charming are implemented in Python, there's plan to rewrite backend in Rush or C++ and refactor some render algorithms such as folygon filling to obtain a better performance.
- **API Enhancement**: Accroding to the feature of terminal, add more cool APIs.
- **More Examples**: Write more interesting examples about *ascii art animation**,  **character-style generative art**, **terminal game** and **expressive data visulization**.
- **Better Documatation**: Write usages, parameters, returens, examples for each API.
