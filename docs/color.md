---
id: color
sidebar_label: Color
hide_title: True
---

# Color

The biggest difference between Charming or Processing is the definition of color, which make Charming so unique to some extend.

In Processing, a color normally has three or four channels: `(r, g, b)` or `(r,g, b, a)` in RGB color mode and `(h, s, b)` or `(h, s, b, a)` in HSB mode, each channel is represented by a number.

```java
/* processing color*/

size(900, 300);
stroke(255, 0, 0);
fill(255, 255, 0);
rect(0, 0, 100, 100);
```

![processnig color](https://raw.githubusercontent.com/charming-art/public-files/master/processing_color.png)

## Ansi mode

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

## RGB color mode

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

## HSB color mode

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

## Double mode

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

:::important
**Charming can't always get the right width of unicodes, so if you find something wrong when using unicodes, you can declare the width of that unicode directly.**
:::

```py
''' charming: double mode'''

app.full_screen(app.DOUBLE)

app.stroke('@', fg=app.GREEN)

# use a tuple to declare the width of that unicode
app.fill(('⏰', 2), bg=app.BLUE)
app.square(0, 0, 10)

app.run()
```
