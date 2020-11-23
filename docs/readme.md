# Documation

## Overview

Charming implements most of Processing's APIs related to 2D, all of the supported API are list below.
Currently the API reference of Charming is not detailed, you can take [Processing Documatation](https://processing.org/reference/) as a reference. And there are some basic [test samples](../tests/) you can take a look.

After reading this, if you have problems with APIs, feel free to open issues or just wait for the outcoming full documation.

## Difference

If you are familiar with Processing or P5js, there are some main differences you should pay attention to.

### Color

In Processing, you can use three number((r, g, b) or (h, s,b)) to represent a color or take them as parameters to color-related APIs, such as `fill(0, 0, 0)` or `stroke(0, 0, 0). But in Charming, you also need three channels to represet a color or put them to color-related APIs:

- `ch`: the ansi, unicode or cjk.
- `fg`: a number(0 ~ 255 by default) if the color mode is ansi, a tuple which lenght is 1 or 3 if the color mode is HSB or RGB.
- `bg`: a number(0 ~ 255 by default) if the color mode is ansi, a tuple which lenght is 1 or 3 if the color mode is HSB or RGB.

```py
# ansi mode
app.fill('c', app.RED, app.BLUE)
app.stroke('酷', 100, 200)

# rgb mode
app.color_mode(app.RGB)
app.background('🚀', (255, 0, 0), (100,))

# hsb mode
app.color_mode(app.HSB)
c = app.CColor('🚀', (255, 0, 0), (100,))
app.background(c)
```

### Name

All the APIs in Processing are like `aaaBBB`, but in Charming they are like `aaa_bbb`. For example, `ellipse_mode` in Charming is equals to `ellipseMode` in Processing and `begin_shape` is equals to `beginShape`.

### Global Var

In Processing, you can use some global var directly, such as `width`, `height`... But in Charming, you should call a method to get the global var. For example, you can get `width` by call `get_width()` or calling `get_mouse_x()` to get `mouseX`.

### Context Manager

In Processing, you need to call a method to open a context and fllowed by a close context function, such as `beginShape` with `endShape`. But with the help of context manager in Python, you can use `with` to open a context.
  
```py

with app.open_shape():
    '''
    app.begin_shape()
    ...
    ...
    app.shape_shape()
    '''
    pass

with app.open_context():
    '''
    app.push()
    ...
    ...
    app.pop()
    '''
    pass

with app.open_contour():
    '''
    app.begin_contour()
    ...
    ...
    app.end_contour()
    '''
    pass
```

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

Examples: [active](../tests/test_structure_active.py), [static](../tests/test_structure_static.py)

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
  
Examples: [2d primitives](../tests/test_shape_primitives.py)

#### Attributes

- ellipse_mode()
- rect_mode()
- stroke_weight()

Examples: [attributes](../tests/test_shape_attributes.py)

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
  
Examples: [vertex](../tests/test_shape_vertex.py)

#### Curves

- bezier()
- bezier_point()
- bezier_tangent()
- curve()
- curve_point()
- curve_tangent()
- curve_tightness()

Examples: [curve](../tests/test_shape_curve.py), [bezier](../tests/test_shape_bezier.py)

### Transform

- translate()
- scale()
- rotate()
- shear_x()
- shear_y()
  
Examples: [transform](../tests/test_transform.py)

### Color

- background()
- fill()
- no_fill()
- no_stroke()
- stroke()
- color_mode()
- CColor
- lerp_color()

Examples: [color](../tests/test_color.py), [ansi mode](../tests/test_color_mode_ansi.py), [rgb mode](../tests/test_color_mode_rgb.py), [hsb mode](../tests/test_color_mode_hsb.py)

### Events

#### Keyboard

- get_key()
- get_key_code()
- get_key_pressed()
- key_pressed()
- key_typed()
- key_relesed()

Examples: [keyboard](../tests/test_event_keyboard.py)
  
#### Mouse

- get_mouseX()
- get_mouseY()
- get_mouse_pressed()
- get_mouse_button()
- mouse_clickd()
- mouse_pressed()
- mouse_released()

Examples: [mouse](../tests/test_event_mouse.py)

#### Cursor

- get_cursorX()
- get_cursorY()
- get_pcursorX()
- get_pcursorY()
- cursor_moved()
- get_cursor_moved()

Examples: [cursor](../tests/test_event_cursor.py)

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

Examples: [single mode](../tests/test_environment_single.py), [double mode](../tests/test_environment_double.py)

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

Examples: [random](../tests/test_math.random.py)

#### Typography

- text()
- text_width()
- text_align()
- text_size()
- text_height()
- get_font_list()
- text_font()

Examples: [ascii](../tests/test_typography_ascii.py), [words](../tests/test_typography_words.py), [clock](../tests/test_time.py)

### Image
  
- CImage
- image()
- image_mode()
- load_image()
- no_tint()
- tint()

Examples: [image](../tests/test_image.py)

### Time

- day()
- hour()
- millis()
- minute()
- month()
- second()
- year()
  
Examples: [clock](../tests/test_time.py)

### Helpers

- print
- no_check

Examples: [print](../tests/test_helper_print.py), [no check](../tests/test_helper_no_check.py)

### Constants

#### PI

- HALF_PI
- PI
- QUARTER_PI
- TAU
- TWO_PI

Examples: [transform](../tests/test_transform.py)

#### Close Mode

- OPEN
- CLOSE
  
Examples: [2d primitives](../tests/test_shape_primitives.py)

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

Examples: [2d primitives](../tests/test_shape_primitives.py), [vertex](../tests/test_shape_vertex.py)

#### Shape Mode

- CORNERS
- CORNER
- CENTER
- RADIUS
- CHORD

Examples: [attributes](../tests/test_shape_attributes.py), [image](../tests/test_image.py)

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

Examples: [ascii](../tests/test_typography_ascii.py), [words](../tests/test_typography_words.py), [clock](../tests/test_time.py)

#### Ansi Color

- RED
- BLACK
- CYAN
- YELLOW
- GREEN
- BLUE
- WHITE
- MAGENTA

Examples: [ansi mode](../tests/test_color_mode_ansi.py)

- ANSI
- RGB
- HSB

Examples: [ansi mode](../tests/test_color_mode_ansi.py), [rgb mode](../tests/test_color_mode_rgb.py), [hsb mode](../tests/test_color_mode_hsb.py)

#### Mode

- DOUBLE
- SINGLE

Examples: [single mode](../tests/test_environment_single.py), [double mode](../tests/test_environment_double.py)

#### Mouse Button

- LEFT
- RIGHT

Examples: [mouse](../tests/test_event_mouse.py)

####**** Key Code

- TAB
- ENTER
- ESCAPE
- SPACE
- BACKSPACE
- LEFT
- UP
- RIGHT
- DOWN
  
Examples: [keyboard](../tests/test_event_keyboard.py)
