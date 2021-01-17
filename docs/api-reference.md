---
id: api-reference
sidebar_label: API Reference
hide_title: True
---

# API Reference

Charming implements most of Processing's APIs related to 2D, all of the supported APIs are list below. You can take [Processing Documentation](https://processing.org/reference/) as a reference, and take a look at some basic [test samples](https://github.com/charming-art/charming/blob/master/tests/) to be familiar with the supported APIs

## Structure

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

*Examples*: [active mode](https://github.com/charming-art/charming/blob/master/tests/test_structure_active.py), [static mode](https://github.com/charming-art/charming/blob/master/tests/test_structure_static.py)

## Shape

### 2D Primitives

- arc()
- circle()
- ellipse()
- line()
- point()
- quad()
- rect()
- square()
- triangle()
  
*Examples*: [2d primitives](https://github.com/charming-art/charming/blob/master/tests/test_shape_primitives.py)

### Attributes

- ellipse_mode()
- rect_mode()
- stroke_weight()

*Examples*: [attributes](https://github.com/charming-art/charming/blob/master/tests/test_shape_attributes.py)

### Vertex

- begin_contour()
- begin_shape()
- bezier_vertex()
- curve_vertex()
- end_contour()
- end_shape()
- vertex()
- open_shape()
- open_contour()
  
*Examples*: [vertex](https://github.com/charming-art/charming/blob/master/tests/test_shape_vertex.py)

### Curves

- bezier()
- bezier_point()
- bezier_tangent()
- curve()
- curve_point()
- curve_tangent()
- curve_tightness()

*Examples*: [curve](https://github.com/charming-art/charming/blob/master/tests/test_shape_curve.py), [bezier](https://github.com/charming-art/charming/blob/master/tests/test_shape_bezier.py)

## Transform

- translate()
- scale()
- rotate()
- shear_x()
- shear_y()
  
*Examples*: [transform](https://github.com/charming-art/charming/blob/master/tests/test_transform.py)

## Color

- CColor()
- background()
- fill()
- no_fill()
- no_stroke()
- stroke()
- color_mode()
- lerp_color()

*Examples*: [color](https://github.com/charming-art/charming/blob/master/tests/test_color.py), [ansi mode](https://github.com/charming-art/charming/blob/master/tests/test_color_mode_ansi.py), [rgb mode](https://github.com/charming-art/charming/blob/master/tests/test_color_mode_rgb.py), [hsb mode](https://github.com/charming-art/charming/blob/master/tests/test_color_mode_hsb.py)

## Events

### Keyboard

- get_key()
- get_key_code()
- get_key_pressed()
- key_pressed()
- key_typed()
- key_relesed()

*Examples*: [keyboard](https://github.com/charming-art/charming/blob/master/tests/test_event_keyboard.py)
  
### Mouse

- get_mouseX()
- get_mouseY()
- get_mouse_pressed()
- get_mouse_button()
- mouse_clickd()
- mouse_pressed()
- mouse_released()

*Examples*: [mouse](https://github.com/charming-art/charming/blob/master/tests/test_event_mouse.py)

### Cursor

- get_cursorX()
- get_cursorY()
- get_pcursorX()
- get_pcursorY()
- cursor_moved()
- cursor_pressed()
- get_cursor_moved()

*Examples*: [cursor](https://github.com/charming-art/charming/blob/master/tests/test_event_cursor.py)

## Environment

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

*Examples*: [single mode](https://github.com/charming-art/charming/blob/master/tests/test_environment_single.py), [double mode](https://github.com/charming-art/charming/blob/master/tests/test_environment_double.py)

## Math

- CVector()

### Calculation

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

### Trigonometry

- acos()
- asin()
- atan()
- atan2()
- cos()
- degrees()
- radians()
- sin()
- tan()

### Random

- noise()
- noise_detail()
- noise_seed()
- random()
- random_gaussian()
- random_seed()

*Examples*: [random](https://github.com/charming-art/charming/blob/master/tests/test_math_random.py)

## Typography

- text()
- text_width()
- text_align()
- text_size()
- text_height()
- get_font_list()
- text_font()

*Examples*: [ascii](https://github.com/charming-art/charming/blob/master/tests/test_typography_ascii.py), [words](https://github.com/charming-art/charming/blob/master/tests/test_typography_words.py), [clock](https://github.com/charming-art/charming/blob/master/tests/test_time.py)

## Image
  
- CImage
- image()
- image_mode()
- load_image()
- no_tint()
- tint()

*Examples*: [image](https://github.com/charming-art/charming/blob/master/tests/test_image.py)

## Time

- day()
- hour()
- millis()
- minute()
- month()
- second()
- year()
  
*Examples*: [clock](https://github.com/charming-art/charming/blob/master/tests/test_time.py)

## Helpers

- print()
- no_check()

*Examples*: [print](https://github.com/charming-art/charming/blob/master/tests/test_helper_print.py), [no check](https://github.com/charming-art/charming/blob/master/tests/test_helper_no_check.py)

## Constants

### PI

- HALF_PI
- PI
- QUARTER_PI
- TAU
- TWO_PI

*Examples*: [transform](https://github.com/charming-art/charming/blob/master/tests/test_transform.py)

### Close mode

- OPEN
- CLOSE
  
*Examples*: [2d primitives](https://github.com/charming-art/charming/blob/master/ests/test_shape_primitives.py)

### Primitive type

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

*Examples*: [2d primitives](https://github.com/charming-art/charming/blob/master/tests/test_shape_primitives.py), [vertex](https://github.com/charming-art/charming/blob/master/tests/test_shape_vertex.py)

### Shape mode

- CORNERS
- CORNER
- CENTER
- RADIUS
- CHORD

*Examples*: [attributes](https://github.com/charming-art/charming/blob/master/tests/test_shape_attributes.py), [image](https://github.com/charming-art/charming/blob/master/tests/test_image.py)

### Text

- LEFT
- RIGHT
- MIDDLE
- TOP
- CENTER
- BOTTOM
- NORMAL
- BIG
- LARGE

*Examples*: [ascii](https://github.com/charming-art/charming/blob/master/tests/test_typography_ascii.py), [words](https://github.com/charming-art/charming/blob/master/tests/test_typography_words.py), [clock](https://github.com/charming-art/charming/blob/master/tests/test_time.py)

### Ansi color

- RED
- BLACK
- CYAN
- YELLOW
- GREEN
- BLUE
- WHITE
- MAGENTA

*Examples*: [ansi mode](https://github.com/charming-art/charming/blob/master/tests/test_color_mode_ansi.py)

- ANSI
- RGB
- HSB

*Examples*: [ansi mode](https://github.com/charming-art/charming/blob/master/tests/test_color_mode_ansi.py), [rgb mode](https://github.com/charming-art/charming/blob/master/tests/test_color_mode_rgb.py), [hsb mode](https://github.com/charming-art/charming/blob/master/tests/test_color_mode_hsb.py)

### Mode

- DOUBLE
- SINGLE

*Examples*: [single mode](https://github.com/charming-art/charming/blob/master/tests/test_environment_single.py), [double mode](https://github.com/charming-art/charming/blob/master/tests/test_environment_double.py)

### Mouse button

- LEFT
- RIGHT

*Examples*: [mouse](https://github.com/charming-art/charming/blob/master/tests/test_event_mouse.py)

### Key code

- TAB
- ENTER
- ESCAPE
- SPACE
- BACKSPACE
- LEFT
- UP
- RIGHT
- DOWN
  
*Examples*: [keyboard](https://github.com/charming-art/charming/blob/master/tests/test_event_keyboard.py)
