# API Refernece

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

- [x] CColor
- [x] background()
- [x] fill()
- [x] no_fill()
- [x] no_stroke()
- [x] stroke()
- [x] color_mode()
  
## Events

### Keyboard

- [x] get_key()
- [x] get_key_code()
- [x] key_typed()
- [x] get_key_pressed()
  
### Mouse

- [x] mouse_clickd()
- [x] mouse_released()
- [x] mouse_pressed()
- [x] get_mouseX()
- [x] get_mouseY()
- [x] get_mouse_pressed()
  
### Cursor

- [ ] get_cursorX()
- [ ] get_cursorY()
- [ ] get_pcursorX()
- [ ] get_pcursorY()
- [ ] cursor_moved()

### Window

- [x] window_resized()

## Environment

- [x] delay()
- [x] cursor()
- [x] get_window_width()
- [x] get_window_height()
- [x] frame_rate()
- [x] full_screen()
- [x] get_frame_count()
- [x] get_frame_rate()
- [x] no_cursor()
- [x] get_height()
- [x] size()
- [x] get_width()
- [x] terminal_size()
- [x] full_terminal()

## Constants

- [x] HALF_PI
- [x] PI
- [x] QUARTER_PI
- [x] TAU
- [x] TWO_PI

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

## Typography

- [x] text()
- [x] text_width()
- [x] text_align()
- [x] text_size()
- [x] text_height()
- [x] get_font_list()
- [x] text_font()

## Image
  
- [x] Image
- [x] image()
- [x] image_mode()
- [x] load_image()
- [x] no_tint()
- [x] tint()
  
## Cells

- [ ] load_cells()
- [ ] get_cells()
- [ ] update_cells()
