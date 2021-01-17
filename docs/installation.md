---
id: installation
title: Installation
---

It is very easy to get started with Charming as long as you install python3 already.

## Requirements

- Charming currently only supports **MacOS**, though it should also work for any other platform that provides a working [curses](https://docs.python.org/3/howto/curses.html) implementation. It soon will support **Windows** and run in **modern browsers**.
- [Python](https://www.python.org/downloads/) version >= 3.6.

## Install from pip

Open a terminal and execute the command as below.

```bash
pip3 install charming --user
```

## First sketch

Create a file named `sketch.py` and copy the code to it and save.

```py
''' sketch.py '''

import charming as app

# draw a rect
app.full_screen()
app.rect(0, 0, 10, 10)

# run the sketch
app.run()
```

Then, open a terminal and run command as below.

```bash
python3 sketch.py
```

🎉 Congratulations to you if you get a simple rectangle in your terminal!

![get started](https://raw.githubusercontent.com/charming-art/public-files/master/get_started.png)
