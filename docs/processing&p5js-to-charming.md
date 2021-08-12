# Processing&P5.js to Charming

Charming implements most of Processing's APIs related to 2D, which can be found [here](./api/readme.md). But due to the grammar differences between Python and Java and different design purposes, there are some differences between the usage of Charming and Processing&P5.js.

This article is going to show the main difference between them and help you migrate from Processing&P5.js to Charming quickly.

- [APIs Names](#apis-names)
- [Register Hooks](#register-hooks)
- [Coordinate System](#coordinate-system)
- [Color System](#color-system)
- [Context Manager](#context-manager)
- [Event](#event)
- [Image](#image)
- [Typography](#typography)

## APIs Names

All the APIs in Processing are like `aaaBbb`, but in Charming they are like `aaa_bbb`. For example, `ellipse_mode` in Charming equals to `ellipseMode` in Processing and `begin_shape` equals to `beginShape`.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

cm.rect_mode(cm.CORNER)
cm.rect(0, 0, 10, 10)

cm.run()
```

There is no `PVector` object in Charming, but you can use `CVector` instead.

```py
import charming as cm

v1 = cm.CVector()
v2 = cm.CVector()
v3 = v1 + v2
```

In Processing, you can use all the global variables directly, such as `width`, `height`, `mouseX`, etc. But in Charming, you should call a method to get the global variable you need. For example, you can get `width` by call `get_width()` or calling `get_mouse_x()` to get `mouseX`.

## Register Hooks

In Processing, you don't have to import all the APIs and it will automatically run hooks such as `setup`, `draw`, `mouseClicked`, etc. But In Charming, you have to import all the APIs at first and use **decorators** to register hooks.

```py
# Import all the APIs and bind them to a namespce.
# You can name it whaterver you like, here name it as 'app'.
import charming as app

# Register setup hook which will excute only once.
@app.setup
def setup():
    app.full_screen()
    app.rect_mode(app.CENTER)

x = 0
speed = 1

# Register draw hook which will loop the code in it.
@app.draw
def draw():
    global x
    app.rect(x, 0, 10, 15)
    x += speed

# Register mouse_clicked hook which will excute when a mouse click event be triggered.
@app.mouse_clicked
def mouse_clicked():
    global speed
    speed += 1

# It is very import to excute run, otherwise nothing magic wll happen.
app.run()
```

## Color System

In Processing, you can use three or four number `(r, g, b)` or `(r, g, b, a)` to represent a color or take them as parameters to color-related APIs, such as `fill(100, 34, 0, 100)` or `stroke(0, 0, 0)`. But in Charming, you need three different channels to represet a color or give them to color-related APIs:

- `ch`: character, ascii code or unicode (including cjk characters or emoji).
- `fg`: foreground color, a number(0 ~ 255 by default) if the color mode is ANSI, a tuple with length equaling to 1or 3 if the color mode is HSB or RGB.
- `bg`: background color, a number(0 ~ 255 by default) if the color mode is ANSI, a tuple with length equaling to 1 or 3 if the color mode is HSB or RGB.

```py
# ansi mode
app.fill('c', app.RED, app.BLUE)
app.stroke('酷', 100, 200)

# rgb mode
app.color_mode(app.RGB)
app.background('🚀', (255, 0, 0), (100,))

# hsb mode
app.color_mode(app.HSB)
# use a CColor object to represent a color
c = app.CColor('🚀', (255, 0, 0), (100,))
app.background(c)
```

## Context Manager

In Processing, you need to call a method to open a context and followed by a close context method, such as `beginShape` with `endShape`. But with the help of context manager in Python, you can use `with` to open a context.
  
```py
# normal way of opening a context
app.begin_shape()
app.vertex(0, 0)
app.vertex(0, 5)
app.vertex(5, 0)
app.end_shape(app.CLOSE)

# open a context with the help of context manager
with app.open_shape(close_mode=app.CLOSE):
    app.vertex(0, 0)
    app.vertex(0, 5)
    app.vertex(5, 0)
```

You can also use `open_context` instead of `push` and `pop` and `open_contour` instead of `begin_contour` and `end_contour`.
