# Charming

Charming(Character Terminal Art Programming) is a coss-platform python package for creating interactive character terminal art program.

## Getting Started

```py
# sketch.py
import charming as app

@app.setup
def foo():
    app.size(100, 100)

@app.draw
def foo():
    app.stroke('#')
    app.fill('@')
    app.rect(0, 0, 20, 20)

app.run()
```

### Terminal

```bash
pip3 install charming
python3 sketch.py
```

### Web

```html
<!-- index.html -->
<html>
    <head>
        <link rel="stylesheet" href="xterm.css" />
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.8.10/brython.min.js"></script>
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.8.10/brython_stdlib.js"></script>
        <script src="xterm.js"></script>
        <script type="text/python" src="charming.py"></script>
    <head>
    <body onload="brython()">
        <script type="text/python" src="sketch.py"></script>
    </body>
</html>
```

```bash
python3 - http.server 8000
```

### Online Editor

Try it one an online editor.

## API Refernece

### Structure

- [x] setup()
- [x] draw()
- [x] run()
- [x] no_loop()
- [x] loop()
- [x] redraw()
- [x] push()
- [x] pop()
- [x] open_context()
- [ ] preload()

### Shape

#### 2D Primitives

- [x] arc()
- [x] circle()
- [x] ellipse()
- [x] line()
- [x] point()
- [x] quad()
- [x] rect()
- [x] square()
- [x] triangle()

#### Attributes

- [x] ellipse_mode()
- [x] rect_mode()
- [x] stroke_weight()

#### Vertex

- [x] begin_contour()
- [x] begin_shape()
- [x] bezier_vertex()
- [x] curve_vertex()
- [x] end_contour()
- [x] end_shape()
- [x] vertex()
- [x] open_shape()
- [x] open_contour()

#### Curves

- [x] bezier()
- [x] bezier_point()
- [x] bezier_tangent()
- [x] curve()
- [x] curve_point()
- [x] curve_tangent()
- [x] curve_tightness()

### Transform

- [x] translate()
- [x] scale()
- [x] rotate()
- [x] shear_x()
- [x] shear_y()
  
### Color

#### Settings

- [x] background()
- [x] fill()
- [x] no_fill()
- [x] no_stroke()
- [x] stroke()

#### Creating && Reading

- [x] color()
- [x] ch()
- [x] bg()
- [x] fg()
  
### Events

#### Keyboard

- [x] get_key()
- [ ] get_key_code()
- [x] key_typed()
- [ ] get_key_pressed()
  
#### Mouse

- [x] mouse_clickd()
- [x] get_mouseX()
- [x] get_mouseY()
- [x] get_pmouseX()
- [x] get_pmouseY()
- [ ] get_mouse_pressed()
  
#### Cursor

- [ ] get_cursorX()
- [ ] get_cursorY()
- [ ] get_pcursorX()
- [ ] get_pcursorY()
- [ ] cursor_moved()

#### Window

- [x] window_resized()

### Environment

- [x] delay()
- [x] cursor()
- [x] get_window_width(): the cols of the termianl
- [x] get_window_height(): the lines of the terminal
- [x] frame_rate()
- [x] full_screen
- [x] get_frame_count()
- [x] get_frame_rate()
- [x] no_cursor()
- [x] get_height()
- [x] size()
- [x] get_width()

### Constants

- [x] HALF_PI
- [x] PI
- [x] QUARTER_PI
- [x] TAU
- [x] TWO_PI

### Math

- [x] CVector

#### Calculation

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

#### Trigonometry

- [x] acos()
- [x] asin()
- [x] atan()
- [x] atan2()
- [x] cos()
- [x] degrees()
- [x] radians()
- [x] sin()
- [x] tan()

#### Random

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
- [x] text_leading()
- [x] text_size()
- [x] text_height()

### Image
  
#### Loading & Displaying

- [ ] image()
- [ ] image_mode()
- [ ] load_image()
- [ ] no_tint()
- [ ] tint()
  
#### Pixels

- [ ] load_pixels()
- [ ] get_pixels()
- [ ] update_pixels()
