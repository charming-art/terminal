# Documentation

This is a rough documentation for Charming. If you still have problems with APIs after reading this documentation, feel free to open any issues or just wait for the outcoming detailed documentation.

## Overview

Charming implements most of Processing's APIs related to 2D, all of the supported APIs are list below.
You can take [Processing Documentation](https://processing.org/reference/) as a reference, and take a look at some basic [test samples](../tests/) to be familiar with the supported APIs.

## Before Start

Before you start reading API reference, it will be very helpful if you get to know the main differences between Charming and Processing.

### Register Hooks

In Processing, you don't have to import all the APIs and it will automatically run hooks such as `setup`, `draw`, `mouseClicked`, etc. But In Charming, you have import all the APIs at first and use decorators to register hooks.

```py
# Import all the APIs and bind to a namespce.
# You can name it whaterver you like, here name it as app.
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

# Register mouse_clicked hook
# which will excute when a mouse click event be triggered.
@app.mouse_clicked
def mouse_clicked():
    global speed
    speed += 1

# It is very import to excute run,
# otherwise nothing magic wll happen.
app.run()
```

### Different Color System

In Processing, you can use three or four number `(r, g, b)` or `(r, g, b, a)` to represent a color or take them as parameters to color-related APIs, such as `fill(100, 34, 0, 100)` or `stroke(0, 0, 0). But in Charming, you need three channels to represet a color or give them to color-related APIs:

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

### APIs Names

All the APIs in Processing are like `aaaBBB`, but in Charming they are like `aaa_bbb`. For example, `ellipse_mode` in Charming is equals to `ellipseMode` in Processing and `begin_shape` is equals to `beginShape`.

### Global Variables

In Processing, you can use all the global variables directly, such as `width`, `height`, `mouseX`, etc. But in Charming, you should call a method to get the global variable you need. For example, you can get `width` by call `get_width()` or calling `get_mouse_x()` to get `mouseX`.

### Context Manager

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

## API reference

### Structure

- setup()
- draw()
- run()
- no_loop()
- loop()
- redraw()
- push()
- pop()
- open_context()
- exit()

*Examples*: [active mode](../tests/test_structure_active.py), [static mode](../tests/test_structure_static.py)

### Shape

#### 2D Primitives

- arc()
- circle()
- ellipse()
- line()
- point()
- quad()
- rect()
- square()
- triangle()
  
*Examples*: [2d primitives](../tests/test_shape_primitives.py)

#### Attributes

- ellipse_mode()
- rect_mode()
- stroke_weight()

*Examples*: [attributes](../tests/test_shape_attributes.py)

#### Vertex

- begin_contour()
- begin_shape()
- bezier_vertex()
- curve_vertex()
- end_contour()
- end_shape()
- vertex()
- open_shape()
- open_contour()
  
*Examples*: [vertex](../tests/test_shape_vertex.py)

#### Curves

- bezier()
- bezier_point()
- bezier_tangent()
- curve()
- curve_point()
- curve_tangent()
- curve_tightness()

*Examples*: [curve](../tests/test_shape_curve.py), [bezier](../tests/test_shape_bezier.py)

### Transform

- translate()
- scale()
- rotate()
- shear_x()
- shear_y()
  
*Examples*: [transform](../tests/test_transform.py)

### Color

- background()
- fill()
- no_fill()
- no_stroke()
- stroke()
- color_mode()
- CColor
- lerp_color()

*Examples*: [color](../tests/test_color.py), [ansi mode](../tests/test_color_mode_ansi.py), [rgb mode](../tests/test_color_mode_rgb.py), [hsb mode](../tests/test_color_mode_hsb.py)

### Events

#### Keyboard

- get_key()
- get_key_code()
- get_key_pressed()
- key_pressed()
- key_typed()
- key_relesed()

*Examples*: [keyboard](../tests/test_event_keyboard.py)
  
#### Mouse

- get_mouseX()
- get_mouseY()
- get_mouse_pressed()
- get_mouse_button()
- mouse_clickd()
- mouse_pressed()
- mouse_released()

*Examples*: [mouse](../tests/test_event_mouse.py)

#### Cursor

- get_cursorX()
- get_cursorY()
- get_pcursorX()
- get_pcursorY()
- cursor_moved()
- get_cursor_moved()

*Examples*: [cursor](../tests/test_event_cursor.py)

### Environment

- cursor()
- frame_rate()
- full_screen()
- get_frame_count()
- get_frame_rate()
- no_cursor()
- get_height()
- get_width()
- size()
- window_resized()
- set_cursor()
- get_window_size()

*Examples*: [single mode](../tests/test_environment_single.py), [double mode](../tests/test_environment_double.py)

### Math

- CVector

#### Calculation

- abs()
- ceil()
- constrain()
- dist()
- exp()
- floor()
- lerp()
- log()
- mag()
- map()
- max()
- min()
- norm()
- pow()
- round()
- sq()
- sqrt()

#### Trigonometry

- acos()
- asin()
- atan()
- atan2()
- cos()
- degrees()
- radians()
- sin()
- tan()

#### Random

- noise()
- noise_detail()
- noise_seed()
- random()
- random_gaussian()
- random_seed()

*Examples*: [random](../tests/test_math.random.py)

#### Typography

- text()
- text_width()
- text_align()
- text_size()
- text_height()
- get_font_list()
- text_font()

*Examples*: [ascii](../tests/test_typography_ascii.py), [words](../tests/test_typography_words.py), [clock](../tests/test_time.py)

### Image
  
- CImage
- image()
- image_mode()
- load_image()
- no_tint()
- tint()

*Examples*: [image](../tests/test_image.py)

### Time

- day()
- hour()
- millis()
- minute()
- month()
- second()
- year()
  
*Examples*: [clock](../tests/test_time.py)

### Helpers

- print
- no_check

*Examples*: [print](../tests/test_helper_print.py), [no check](../tests/test_helper_no_check.py)

### Constants

#### PI

- HALF_PI
- PI
- QUARTER_PI
- TAU
- TWO_PI

*Examples*: [transform](../tests/test_transform.py)

#### Close Mode

- OPEN
- CLOSE
  
*Examples*: [2d primitives](../tests/test_shape_primitives.py)

#### Primitive Type

- POLYGON
- POINTS
- LINES
- TRIANGLES
- TRIANGLE_STRIP
- TRIANGLE_FAN
- QUADS
- QUAD_STRIP
- PIE
- OPEN

*Examples*: [2d primitives](../tests/test_shape_primitives.py), [vertex](../tests/test_shape_vertex.py)

#### Shape Mode

- CORNERS
- CORNER
- CENTER
- RADIUS
- CHORD

*Examples*: [attributes](../tests/test_shape_attributes.py), [image](../tests/test_image.py)

#### Text

- LEFT
- RIGHT
- MIDDLE
- TOP
- CENTER
- BOTTOM
- NORMAL
- BIG
- LARGE

*Examples*: [ascii](../tests/test_typography_ascii.py), [words](../tests/test_typography_words.py), [clock](../tests/test_time.py)

#### Ansi Color

- RED
- BLACK
- CYAN
- YELLOW
- GREEN
- BLUE
- WHITE
- MAGENTA

*Examples*: [ansi mode](../tests/test_color_mode_ansi.py)

- ANSI
- RGB
- HSB

*Examples*: [ansi mode](../tests/test_color_mode_ansi.py), [rgb mode](../tests/test_color_mode_rgb.py), [hsb mode](../tests/test_color_mode_hsb.py)

#### Mode

- DOUBLE
- SINGLE

*Examples*: [single mode](../tests/test_environment_single.py), [double mode](../tests/test_environment_double.py)

#### Mouse Button

- LEFT
- RIGHT

*Examples*: [mouse](../tests/test_event_mouse.py)

#### Key Code

- TAB
- ENTER
- ESCAPE
- SPACE
- BACKSPACE
- LEFT
- UP
- RIGHT
- DOWN
  
*Examples*: [keyboard](../tests/test_event_keyboard.py)