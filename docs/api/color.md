# Color

Methods for creating, reading and setting colors.

<a name="ccolor" href="#ccolor">#</a> cm.**CColor**(*ch*=" "[, *fg*[, *bg*]])

Creates colors for storing in variables of the color datatype. The `fg` or `bg` parameters are interpreted as ANSI, RGB or HSB values depending on the current `color_mode`.

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

- `fill(ch=" "[, fg[, bg]])`
- `no_fill()`
- `no_stroke()`
- `stroke(ch="*"[, fg[, bg]])`
- `color_mode(mode=ANSI | RGB | HSB[, max1[, max2, [, max3]]])`
- `lerp_color(start, stop, amt)`

**Examples**

- [Color](https://github.com/charming-art/charming/blob/master/tests/test_color.py)
- [ANSI Mode](https://github.com/charming-art/charming/blob/master/tests/test_color_mode_ansi.py)
- [RGB Mode](https://github.com/charming-art/charming/blob/master/tests/test_color_mode_rgb.py)
- [HSB Mode](https://github.com/charming-art/charming/blob/master/tests/test_color_mode_hsb.py)