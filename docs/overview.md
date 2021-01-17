---
id: overview
title: Overview
slug: /
---

Charming is a creative coding language designed for **interactive character terminal art**.

It currently written in Python and provides Processing-like APIs, which aims to help artists, designers, educators, beginners, and anyone else to easily create:

- ASCII Art Animation
- Character-Style Generative Art
- Terminal Game Application
- Expressive Data Visualization

## Quick example

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

<!-- ## Features

## Comparison with other tools -->
