<center>
<h1>Charming</h1>
<p style="font-size:16px;font-weight:bold"><a href="https://charming-art.github.io/">Home |</a><a href="https://charming-art.github.io/docs"> Documentation |</a><a href="https://charming-art.github.io/gallery"> Gallery</a></p>
<a href="https://charming-art.github.io/"><img src="https://raw.githubusercontent.com/charming-art/public-files/master/home_code.png" alt="Charming" height="300"></a>&ensp;
<a href="https://charming-art.github.io/"><img src="https://raw.githubusercontent.com/charming-art/public-files/master/welcome.gif" alt="Charming" height="300"></a>
</center>

## Overview

Charming is a creative coding language designed for **Character Terminal Art Programming**.

It currently written in Python and provides Processing-like APIs, which aims to help artists, designers, educators, beginners, and anyone else to easily create:

- ASCII Art Animation
- Character-Style Generative Art
- Terminal Game Application
- Expressive Data Visualization

## Installation

- **Supported OS**: Charming currently only supports **MacOS**, though it should also work for any other platform that provides a working [curses](https://docs.python.org/3/howto/curses.html) implementation. It soon will support **Windows** and run in **Modern Browsers**.
- **Python**: 3.6/3.7/3.8

```bash
pip3 install charming --user
```

## Quick example

Create a new file named `sketch.py` and copy the following code to it.

```py
''' sketch.py '''

import charming as app

# draw a rect
app.full_screen()
app.rect(0, 0, 10, 10)

# run the sketch
app.run()
```

Run `python3 sketch.py` and congratulations to you if you get a simple rectangle in your terminal!

![get started](https://raw.githubusercontent.com/charming-art/public-files/master/get_started.png)

## License

[LGPL-2.1 License](https://github.com/charming-art/charming/blob/master/LICENSE)
