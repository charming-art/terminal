# Charming

Charming(Character Terminal Art Programming) is a coss-platform python package for creating interactive character terminal art program.

## Getting Started

```py
# sketch.py
import charming as app

@app.setup
def setup():
    app.size(100, 100)

@app.draw
def draw():
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

### Shape

- [ ] create_shape()
- [ ] CShape()

#### 2D Primitives

- [ ] arc()
- [ ] circle()
- [ ] ellipse()
- [x] line()
- [ ] point()
- [ ] quad()
- [ ] rect()
- [ ] square()
- [ ] triangle()

#### Attributes

- [ ] ellipse_mode()
- [ ] rect_mode()
- [ ] stroke_weight()

#### Vertex

- [ ] begin_contour()
- [ ] begin_shape()
- [ ] bezier_vertex()
- [ ] curve_vertex()
- [ ] end_contour()
- [ ] end_shape()
- [ ] quadratic_vertex()
- [ ] vertex()

#### Curves

- [ ] bezier()
- [ ] bezier_detail()
- [ ] bezier_point()
- [ ] bezier_tangent()
- [ ] curve()
- [ ] curve_detail()
- [ ] curve_point()
- [ ] curve_tangent()
- [ ] curve_tightness()

### Transform

- [ ] apply_matrix()
- [ ] pop_matrix()
- [x] translate()
- [x] scale()
- [x] rotate()
- [ ] shear_x()
- [ ] shear_y()
  
### Color

#### Settings

- [ ] background()
- [ ] clear()
- [ ] fill()
- [ ] no_fill()
- [ ] no_stroke()
- [ ] stroke()

#### Creating && Reading

- [ ] color()
- [ ] ch()
- [ ] bg()
- [ ] fg()
  
### Events

#### Keyboard

- [x] get_key()
- [ ] get_key_code()
- [x] key_typed()
- [ ] is_key_pressed()
  
#### Mouse

- [x] mouse_clickd()
- [x] get_mouseX()
- [x] get_mouseY()
- [x] get_pmouseX()
- [x] get_pmouseY()
- [ ] is_mouse_pressed()
  
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

CVector

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

- [ ] noise()
- [ ] noise_detail()
- [ ] noise_seed()
- [ ] random()
- [ ] random_gaussian()
- [ ] random_seed()

### Typography

- [ ] text()
- [ ] text_width()
- [ ] text_align()
- [ ] text_leading()
- [ ] text_size()
- [ ] text_height()

### Image

- [ ] create_image()
- [ ] CImage
  
#### Loading & Displaying

- [ ] image()
- [ ] image_mode()
- [ ] load_image()
- [ ] no_tint()
- [ ] request_image()
- [ ] tint()
  
#### Textures

- [ ] texture()
- [ ] texture_mode()
- [ ] texture_wrap()
  
#### Pixels

- [ ] blend()
- [ ] copy()
- [ ] filter()
- [ ] get()
- [ ] load_pixels()
- [ ] pixels[]
- [ ] set()
- [ ] update_pixels()
