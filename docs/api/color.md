# Color

Methods for creating, reading and setting colors.

<a name="ccolor" href="#ccolor">#</a> cm.**CColor**(*ch*=" "[, *fg*[, *bg*]])

Creates colors for storing in variables of the color data type. The `fg` or `bg` parameters are interpreted as ANSI, RGB or HSB values depending on the current `color_mode`.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

c0 = cm.CColor()
c1 = cm.CColor('@')
c2 = cm.CColor('@', cm.RED)
c3 = cm.CColor('@', cm.RED, cm.YELLOW)

cm.stroke(c0)
cm.point(0, 0) # nothing

cm.stroke(c1)
cm.point(1, 1) # ('@', cm.WHITE, cm.BLACK)

cm.stroke(c2)
cm.point(2, 2) # ('@', cm.RED, cm.BLACK)

cm.stroke(c3)
cm.point(3, 3) # ('@', cm.RED, cm.YELLOW)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_ccolor.png" width="100%"/>

<a name="background" href="#background">#</a> cm.**background**(*ch*=" "[, *fg*[, *bg*]])<br>
<a name="background" href="#background">#</a> cm.**background**(*ccolor*)

Sets the color used for the background of terminal. The `fg` or `bg` parameters are interpreted as ANSI, RGB or HSB values depending on the current `color_mode`.

This function is typically used within draw() to clear the display window at the beginning of each frame, but it can be used inside setup() to set the background on the first frame of animation or if the background need only be set once.

```py
import charming as cm


@cm.setup
def setup():
    c = cm.CColor('*')
    cm.full_screen()
    cm.frame_rate(2)
    cm.no_cursor()
    cm.background(c)  # use CColor


x = 0


@cm.draw
def draw():
    global x
    x += 1
    t = cm.get_frame_count() % 3

    if t == 0:
        cm.background('@')  # one channel
    elif t == 1:
        cm.background('+', cm.BLUE)  # two channel
    else:
        cm.background('-', cm.RED, cm.BLUE)  # three channel


    cm.fill('0', cm.YELLOW, cm.RED)
    cm.stroke('1', cm.GREEN, cm.BLUE)
    cm.rect(0, 0, 5, 5)


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_background.gif" width="100%"/>

<a name="fill" href="#fill">#</a> cm.**fill**(*ch*=" "[, *fg*[, *bg*]])

Sets the color used to fill shapes. The `fg` or `bg` parameters are interpreted as ANSI, RGB or HSB values depending on the current `color_mode`.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

cm.fill('@', cm.RED, cm.BLUE)
cm.rect(0, 0, 10, 5)

cm.fill('O', cm.YELLOW, cm.CYAN)
cm.rect(20, 0, 10, 5)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_fill.png" width="100%"/>

<a name="no_fill" href="#no_fill">#</a> cm.**no_fill**()

Disables filling shapes. If both `no_stroke()` and `no_fill()` are called, nothing will be drawn to the screen.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

cm.fill('@', cm.RED, cm.BLUE)
cm.rect(0, 0, 10, 5)

cm.no_fill()
cm.rect(20, 0, 10, 5)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_no_fill.png" width="100%"/>

<a name="no_stroke" href="#no_stroke">#</a> cm.**no_stroke**()

Disables drawing the stroke (outline). If both `no_stroke()` and `no_fill()` are called, nothing will be drawn to the screen.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

cm.fill('@', cm.RED, cm.BLUE)
cm.rect(0, 0, 10, 5)

cm.no_stroke()
cm.rect(20, 0, 10, 5)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_no_stroke.png" width="100%"/>

<a name="stroke" href="#stroke">#</a> cm.**stroke**(*ch*="*"[, *fg*[, *bg*]])

Sets the color used to draw lines and borders around shapes. The `fg` or `bg` parameters are interpreted as ANSI, RGB or HSB values depending on the current `color_mode`.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

cm.stroke('@', cm.RED, cm.BLUE)
cm.rect(0, 0, 10, 5)

cm.stroke('O', cm.YELLOW, cm.CYAN)
cm.rect(20, 0, 10, 5)

cm.run()
```

<a name="color_mode" href="#color_mode">#</a> cm.**color_mode**(*mode*=ANSI | RGB | HSB[, *max1*[, *max2*, [, *max3*]]])

color_mode() changes the way Charming interprets color data. By default, the parameters for fill(), stroke(), background(), and color() are defined by values between 0 and 255 using ANSI color.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

for i in range(256):
    x = i % 32
    y = i // 32
    cm.stroke(' ', i, i)
    cm.point(x, y)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_color_mode_ansi_256.png" width="100%"/>

To make it easier to use ANSI color, there are some predefined constants which can be used directly as below.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

# basic colors
colors = [
    cm.RED,
    cm.BLACK,
    cm.CYAN,
    cm.YELLOW,
    cm.GREEN,
    cm.BLUE,
    cm.WHITE,
    cm.MAGENTA
]

cm.stroke_weight(1)
for i, c in enumerate(colors):
    x = 5
    y = 2
    cm.stroke("@", c, c)
    cm.point(i * 5 + x , y)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_color_mode_ansi_baisc.png" width="100%"/>

Setting `color_mode(HSB)` lets you use the HSB system instead. In this situation, each color is represented by three-elements tuple `(hue, saturation, brightness)`. The hue channel is between 0 and 255, and the saturation or brightness channel is between 0 and 100. It is useful to draw a rainbow.

```py
import charming as cm

cm.full_screen()
cm.color_mode(cm.HSB)
cm.no_cursor()


# rainbows
w = 30
h = 360 / w

for hue in range(360):
    i = hue % w
    j = hue // w
    cm.stroke(" ", (hue, 100, 100), (hue, 100, 100))
    cm.point(i, j)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_color_mode_hsb.png" width="100%"/>

Setting `color_mode(RGB)` lets you use the HSB system instead. In this situation, each color is represented by three-elements tuple `(red, green, blue)`. The red, green, blue channels are all between 0 and 255. `(c,)` is short for `(c, c, c)`. It can be used to draw color with only one channel.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.color_mode(cm.RGB)

n = 7
cm.stroke_weight(1)

for i in range(n):
    c = cm.map(i, 0, n, 0, 255)
    cm.stroke(" ", (c, 0, 0), (c, 0, 0))
    cm.point(i * 5 + 5, 2)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_color_mode_rgb_red.png" width="100%"/>

It also can be used to draw gray colors.

```py
import charming as cm

cm.full_screen()
cm.color_mode(cm.RGB)
cm.no_cursor()

n = 7
cm.stroke_weight(1)

for i in range(n):
    c = cm.map(i, 0, n, 0, 255)
    cm.stroke("@", (c,), (c,))
    cm.point(i * 5 + 5, 2)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_color_mode_rgb_gray.png" width="100%"/>

<a name="lerp_color" href="#lerp_color">#</a> cm.**lerp_color**(*start*, *stop*, *amt*)

Blends two colors to find a third color somewhere between them. The amt parameter is the amount to interpolate between the two values where 0.0 equal to the first color, 0.1 is very near the first color, 0.5 is halfway in between, etc.

Noticed that not only does it interpolate color `bg` and `fg`, it also will interpolates `ch` as well.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

start = cm.CColor('a', cm.BLUE, cm.RED)  # start color
end = cm.CColor('z', cm.GREEN, cm.YELLOW)  # end color

cm.stroke_weight(1)
n = 10
for i in range(n):
    t = i / n
    c = cm.lerp_color(start, end, t)
    cm.stroke(c)
    cm.point(i * 5 + 5, 2)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_lerp_color_ansi.png" width="100%"/>

It also can be used to interpolate color in RGB and HSB color mode.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.color_mode(cm.RGB)

start = cm.CColor('a', (0,), (255, 0, 0))
end = cm.CColor('z', (255, 255, 0), (0,))
n = 10

for i in range(n):
    t = i / n
    c = cm.lerp_color(start, end, t)
    cm.stroke_weight(1)
    cm.stroke(c)
    cm.point(i * 5 + 5, 2)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_lerp_color_rgb.png" width="100%"/>