# API reference

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

### Attributes

- ellipse_mode()
- rect_mode()
- stroke_weight()

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

### Curves

- bezier()
- bezier_point()
- bezier_tangent()
- curve()
- curve_point()
- curve_tangent()
- curve_tightness()

## Transform

- translate()
- scale()
- rotate()
- shear_x()
- shear_y()
  
## Color

- background()
- fill()
- no_fill()
- no_stroke()
- stroke()
- color_mode()
- CColor
- lerp_color()

## Events

### Keyboard

- get_key()
- get_key_code()
- get_key_pressed()
- key_pressed()
- key_typed()
- key_relesed()
  
### Mouse

- get_mouseX()
- get_mouseY()
- get_mouse_pressed()
- get_mouse_button()
- mouse_clickd()
- mouse_pressed()
- mouse_released()
  
### Cursor

- get_cursorX()
- get_cursorY()
- get_pcursorX()
- get_pcursorY()
- cursor_moved()
- get_cursor_moved()

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

## Math

- CVector

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

### Typography

- text()
- text_width()
- text_align()
- text_size()
- text_height()
- get_font_list()
- text_font()

## Image
  
- CImage
- image()
- image_mode()
- load_image()
- no_tint()
- tint()

## Time

- day()
- hour()
- millis()
- minute()
- month()
- second()
- year()

## Helpers

- print
- check_params
  
## Constants

### PI

- [x] HALF_PI
- [x] PI
- [x] QUARTER_PI
- [x] TAU
- [x] TWO_PI

### Close Mode

- [x] OPEN
- [x] CLOSE

### Primitive Type

- [x] POLYGON
- [x] POINTS
- [x] LINES
- [x] TRIANGLES
- [x] TRIANGLE_STRIP
- [x] TRIANGLE_FAN
- [x] QUADS
- [x] QUAD_STRIP

### Shape Mode

- [x] CORNERS
- [x] CORNER
- [x] CENTER
- [x] RADIUS
- [x] CHORD
- [x] PIE
- [x] OPEN

### Text

- [x] LEFT
- [x] RIGHT
- [x] MIDDLE
- [x] TOP
- [x] CENTER
- [x] BOTTOM
- [x] NORMAL
- [x] BIG
- [x] LARGE

### Ansi Color

- [x] RED
- [x] BLACK
- [x] CYAN
- [x] YELLOW
- [x] GREEN
- [x] BLUE
- [x] WHITE
- [x] MAGENTA

### Color Mode

- [x] ANSI
- [x] RGB
- [x] HSB

### Mode

- [x] DOUBLE
- [x] SINGLE

### Mouse Button

- [x] LEFT
- [x] RIGHT

### Key Code

- [x] TAB
- [x] ENTER
- [x] ESCAPE
- [x] SPACE
- [x] BACKSPACE
- [x] LEFT
- [x] UP
- [x] RIGHT
- [x] DOWN
