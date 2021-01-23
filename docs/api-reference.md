---
id: api-reference
sidebar_label: API Reference
hide_title: True
---

# API Reference

Charming implements most of Processing's APIs related to 2D, all of the supported APIs are list below. You can take [Processing Documentation](https://processing.org/reference/) as a reference, and take a look at some basic [test samples](https://github.com/charming-art/charming/blob/master/tests/) to be familiar with the supported APIs

## Structure

- `setup(f)`
- `draw(f)`
- `run()`
- `no_loop()`
- `loop()`
- `redraw()`
- `push()`
- `pop()`
- `open_context()`
- `exit()`

Examples: [active mode](https://github.com/charming-art/charming/blob/master/tests/test_structure_active.py), [static mode](https://github.com/charming-art/charming/blob/master/tests/test_structure_static.py)

## Shape

### 2D Primitives

- `arc(a, b, c, d, start, stop, mode=OPEN | CHORD | PIE)`
- `circle(x, y, extend)`
- `ellipse(a, b, c, d)`
- `line(x1, y1, x2, y2)`
- `point(x, y)`
- `quad(x1, y1, x2, y2, x3, y3, x4, y4)`
- `rect(a, b, c, d)`
- `square(x, y, extend)`
- `triangle(x1, y1, x2, y2, x3, y3)`
  
Examples: [2d primitives](https://github.com/charming-art/charming/blob/master/tests/test_shape_primitives.py)

### Attributes

- `ellipse_mode(mode=CENTER | RADIUS | CORNER | CORNERS)`
- `rect_mode(mode=CORNER | CORNERS | CENTER | RADIUS)`
- `stroke_weight(weight=0)`

Examples: [attributes](https://github.com/charming-art/charming/blob/master/tests/test_shape_attributes.py)

### Vertex

- `begin_contour()`
- `begin_shape(primitive_type=POLYGON | POINTS | LINES | TRIANGLES | TRIANGLE_STRIP | TRIANGLE_FAN | QUADS | QUAD_STRIP)`
- `bezier_vertex(x2, y2, x3, y3, x4, y4)`
- `curve_vertex(x, y)`
- `end_contour()`
- `end_shape(mode=OPEN | CLOSE)`
- `vertex(x, y)`
- `open_shape(primitive_type=POLYGON | POINTS | LINES | TRIANGLES | TRIANGLE_STRIP | TRIANGLE_FAN, mode=OPEN | CLOSE)`
- `open_contour()`
  
Examples: [vertex](https://github.com/charming-art/charming/blob/master/tests/test_shape_vertex.py)

### Curves

- `bezier(x1, y1, x2, y2, x3, y3, x4, y4)`
- `bezier_point(n1, n2, n3, n4, t)`
- `bezier_tangent(n1, n2, n3, n4, t)`
- `curve(x1, y1, x2, y2, x3, y3, x4, y4)`
- `curve_point(n1, n2, n3, n4, t)`
- `curve_tangent(n1, n2, n3, n4, t)`
- `curve_tightness(v)`

Examples: [curve](https://github.com/charming-art/charming/blob/master/tests/test_shape_curve.py), [bezier](https://github.com/charming-art/charming/blob/master/tests/test_shape_bezier.py)

## Transform

- `translate(tx, ty)`
- `scale(sx[, sy])`
- `rotate(x)`
- `shear_x(x)`
- `shear_y(x)`
  
Examples: [transform](https://github.com/charming-art/charming/blob/master/tests/test_transform.py)

## Color

- `CColor(ch=" "[, fg[, bg]])`
- `background(ch=" "[, fg[, bg]])`
- `fill(ch=" "[, fg[, bg]])`
- `no_fill()`
- `no_stroke()`
- `stroke(ch="*"[, fg[, bg]])`
- `color_mode(mode=ANSI | RGB | HSB[, max1[, max2, [, max3]]])`
- `lerp_color(start, stop, amt)`

Examples: [color](https://github.com/charming-art/charming/blob/master/tests/test_color.py), [ansi mode](https://github.com/charming-art/charming/blob/master/tests/test_color_mode_ansi.py), [rgb mode](https://github.com/charming-art/charming/blob/master/tests/test_color_mode_rgb.py), [hsb mode](https://github.com/charming-art/charming/blob/master/tests/test_color_mode_hsb.py)

## Events

### Keyboard

- `get_key()`
- `get_key_code()`
- `get_key_pressed()`
- `key_pressed(f)`
- `key_typed(f)`
- `key_relesed(f)`

Examples: [keyboard](https://github.com/charming-art/charming/blob/master/tests/test_event_keyboard.py)
  
### Mouse

- `get_mouseX()`
- `get_mouseY()`
- `get_mouse_pressed()`
- `get_mouse_button()`
- `mouse_clickd(f)`
- `mouse_pressed(f)`
- `mouse_released(f)`

Examples: [mouse](https://github.com/charming-art/charming/blob/master/tests/test_event_mouse.py)

### Cursor

- `get_cursorX()`
- `get_cursorY()`
- `get_pcursorX()`
- `get_pcursorY()`
- `cursor_moved(f)`
- `cursor_pressed(f)`
- `get_cursor_moved()`

Examples: [cursor](https://github.com/charming-art/charming/blob/master/tests/test_event_cursor.py)

## Environment

- `cursor()`
- `frame_rate(rate)`
- `full_screen(mode=SINGLE | DOUBLIE)`
- `get_frame_count()`
- `get_frame_rate()`
- `no_cursor()`
- `get_height()`
- `get_width()`
- `size(width, height, mode=SINGLE | DOUBLIE)`
- `window_resized(f)`
- `set_cursor(x, y)`
- `get_window_size()`

Examples: [single mode](https://github.com/charming-art/charming/blob/master/tests/test_environment_single.py), [double mode](https://github.com/charming-art/charming/blob/master/tests/test_environment_double.py)

## Math

- `CVector(x=0, y=0)`

### Calculation

- `abs(n)`
- `ceil(n)`
- `constrain(amt, low, high)`
- `dist(x1, y1, x2, y2)`
- `exp(n)`
- `floor(n)`
- `lerp(start, stop, amt)`
- `log(x)`
- `mag(a, b, c=0)`
- `map(value, start1, stop1, start2, stop2)`
- `max(arg1, arg2, *args[, key])`
- `min(arg1, arg2, *args[, key])`
- `norm(value, start, stop)`
- `pow(n, e)`
- `round(n)`
- `sq(n)`
- `sqrt(n)`

### Trigonometry

- `acos(n)`
- `asin(n)`
- `atan(n)`
- `atan2(y, x)`
- `cos(n)`
- `degrees(n)`
- `radians(n)`
- `sin(n)`
- `tan(n)`

### Random

- `noise(x, y=0, z=0)`
- `noise_detail(octaves=4, falloff=0.5)`
- `noise_seed(seed)`
- `random(low[, high])`
- `random_gaussian()`
- `random_seed(seed)`

Examples: [random](https://github.com/charming-art/charming/blob/master/tests/test_math_random.py)

## Typography

- `text(text, x, y)`
- `text_width(text)`
- `text_align(align_x=LEFT | RIGHT | CENTER[, align_y=TOP | BOTTOM | MIDDLE])`
- `text_size(size=NORMAL | BIG |LARGE)`
- `text_height(text)`
- `get_font_list()`
- `text_font(name)`

Examples: [ascii](https://github.com/charming-art/charming/blob/master/tests/test_typography_ascii.py), [words](https://github.com/charming-art/charming/blob/master/tests/test_typography_words.py), [clock](https://github.com/charming-art/charming/blob/master/tests/test_time.py)

## Image
  
- `CImage: object`
- `image(img, a, b[, c[, d]])`
- `image_mode()`
- `load_image()`
- `no_tint()`
- `tint(ch=" "[, fg[, bg]])`

Examples: [image](https://github.com/charming-art/charming/blob/master/tests/test_image.py)

## Time

- `day()`
- `hour()`
- `millis()`
- `minute()`
- `month()`
- `second()`
- `year()`
  
Examples: [clock](https://github.com/charming-art/charming/blob/master/tests/test_time.py)

## Helpers

- `print(*args, **kw)`
- `no_check()`

Examples: [print](https://github.com/charming-art/charming/blob/master/tests/test_helper_print.py), [no check](https://github.com/charming-art/charming/blob/master/tests/test_helper_no_check.py)

## Constants

### PI

- `HALF_PI`
- `PI`
- `QUARTER_PI`
- `TAU`
- `TWO_PI`

Examples: [transform](https://github.com/charming-art/charming/blob/master/tests/test_transform.py)

### Close mode

- `OPEN`
- `CLOSE`
  
*Examples*: [2d primitives](https://github.com/charming-art/charming/blob/master/ests/test_shape_primitives.py)

### Primitive type

- `POLYGON`
- `POINTS`
- `LINES`
- `TRIANGLES`
- `TRIANGLE_STRIP`
- `TRIANGLE_FAN`
- `QUADS`
- `QUAD_STRIP`
- `PIE`
- `OPEN`
- `CHORD`

Examples: [2d primitives](https://github.com/charming-art/charming/blob/master/tests/test_shape_primitives.py), [vertex](https://github.com/charming-art/charming/blob/master/tests/test_shape_vertex.py)

### Shape mode

- `CORNERS`
- `CORNER`
- `CENTER`
- `RADIUS`

Examples: [attributes](https://github.com/charming-art/charming/blob/master/tests/test_shape_attributes.py), [image](https://github.com/charming-art/charming/blob/master/tests/test_image.py)

### Text

- `LEFT`
- `RIGHT`
- `MIDDLE`
- `TOP`
- `CENTER`
- `BOTTOM`
- `NORMAL`
- `BIG`
- `LARGE`

Examples: [ascii](https://github.com/charming-art/charming/blob/master/tests/test_typography_ascii.py), [words](https://github.com/charming-art/charming/blob/master/tests/test_typography_words.py), [clock](https://github.com/charming-art/charming/blob/master/tests/test_time.py)

### Ansi color

- `RED`
- `BLACK`
- `CYAN`
- `YELLOW`
- `GREEN`
- `BLUE`
- `WHITE`
- `MAGENTA`

Examples: [ansi mode](https://github.com/charming-art/charming/blob/master/tests/test_color_mode_ansi.py)

- `ANSI`
- `RGB`
- `HSB`

Examples: [ansi mode](https://github.com/charming-art/charming/blob/master/tests/test_color_mode_ansi.py), [rgb mode](https://github.com/charming-art/charming/blob/master/tests/test_color_mode_rgb.py), [hsb mode](https://github.com/charming-art/charming/blob/master/tests/test_color_mode_hsb.py)

### Mode

- `DOUBLE`
- `SINGLE`

Examples: [single mode](https://github.com/charming-art/charming/blob/master/tests/test_environment_single.py), [double mode](https://github.com/charming-art/charming/blob/master/tests/test_environment_double.py)

### Mouse button

- `LEFT`
- `RIGHT`

Examples: [mouse](https://github.com/charming-art/charming/blob/master/tests/test_event_mouse.py)

### Key code

- `TAB`
- `ENTER`
- `ESCAPE`
- `SPACE`
- `BACKSPACE`
- `LEFT`
- `UP`
- `RIGHT`
- `DOWN`
  
Examples: [keyboard](https://github.com/charming-art/charming/blob/master/tests/test_event_keyboard.py)
