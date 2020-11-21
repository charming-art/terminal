# API reference

## Structure

- [x] setup()
- [x] draw()
- [x] run()
- [x] no_loop()
- [x] loop()
- [x] redraw()
- [x] push()
- [x] pop()
- [x] open_context()

## Shape

### 2D Primitives

- [x] arc()
- [x] circle()
- [x] ellipse()
- [x] line()
- [x] point()
- [x] quad()
- [x] rect()
- [x] square()
- [x] triangle()

### Attributes

- [x] ellipse_mode()
- [x] rect_mode()
- [x] stroke_weight()

### Vertex

- [x] begin_contour()
- [x] begin_shape()
- [x] bezier_vertex()
- [x] curve_vertex()
- [x] end_contour()
- [x] end_shape()
- [x] vertex()
- [x] open_shape()
- [x] open_contour()

### Curves

- [x] bezier()
- [x] bezier_point()
- [x] bezier_tangent()
- [x] curve()
- [x] curve_point()
- [x] curve_tangent()
- [x] curve_tightness()

## Transform

- [x] translate()
- [x] scale()
- [x] rotate()
- [x] shear_x()
- [x] shear_y()
  
## Color

- [x] background()
- [x] fill()
- [x] no_fill()
- [x] no_stroke()
- [x] stroke()
- [x] color_mode()
- [x] CColor
- [x] lerp_color()

## Events

### Keyboard

- [x] get_key()
- [x] get_key_code()
- [x] get_key_pressed()
- [x] key_pressed()
- [x] key_typed()
- [x] key_relesed()
  
### Mouse

- [x] get_mouseX()
- [x] get_mouseY()
- [x] get_mouse_pressed()
- [x] get_mouse_button()
- [x] mouse_clickd()
- [x] mouse_pressed()
- [x] mouse_released()
  
### Cursor

- [x] get_cursorX()
- [x] get_cursorY()
- [x] get_pcursorX()
- [x] get_pcursorY()
- [x] cursor_moved()
- [x] get_cursor_moved()

## Environment

- [x] cursor()
- [x] frame_rate()
- [x] full_screen()
- [x] get_frame_count()
- [x] get_frame_rate()
- [x] no_cursor()
- [x] get_height()
- [x] get_width()
- [x] size()
- [x] window_resized()
- [x] set_cursor()
- [x] get_window_size()

## Math

- [x] CVector

### Calculation

- [x] abs()
- [x] ceil()
- [x] constrain()
- [x] dist()
- [x] exp()
- [x] floor()
- [x] lerp()
- [x] log()
- [x] mag()
- [x] map()
- [x] max()
- [x] min()
- [x] norm()
- [x] pow()
- [x] round()
- [x] sq()
- [x] sqrt()

### Trigonometry

- [x] acos()
- [x] asin()
- [x] atan()
- [x] atan2()
- [x] cos()
- [x] degrees()
- [x] radians()
- [x] sin()
- [x] tan()

### Random

- [x] noise()
- [x] noise_detail()
- [x] noise_seed()
- [x] random()
- [x] random_gaussian()
- [x] random_seed()

### Typography

- [x] text()
- [x] text_width()
- [x] text_align()
- [x] text_size()
- [x] text_height()
- [x] get_font_list()
- [x] text_font()

## Image
  
- [x] CImage
- [x] image()
- [x] image_mode()
- [x] load_image()
- [x] no_tint()
- [x] tint()

## Time

- [x] day()
- [x] hour()
- [x] millis()
- [x] minute()
- [x] month()
- [x] second()
- [x] year()

## Helpers

- [x] debug
  
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
