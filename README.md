# Charming

Charming(Character Art Terminal Programming) is a Python Package for creating interactive character art terminal program.

## Getting Started

```bash
pip3 install charming
```

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

```bash
python3 sketch.py
```

## API Refernece

### Structure

- setup()
- draw()
- run()
- no_loop()
- loop()
- redraw()
- push()
- pop()

### Shape

- create_shape()
- CShape()

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

#### Attributes

- ellipse_mode()
- rect_mode()
- stroke_weight()

#### Vertex

- begin_contour()
- begin_shape()
- bezier_vertex()
- curve_vertex()
- end_contour()
- end_shape()
- quadratic_vertex()
- vertex()

#### Curves

- bezier()
- bezier_detail()
- bezier_point()
- bezier_tangent()
- curve()
- curve_detail()
- curve_point()
- curve_tangent()
- curve_tightness()

### Transform

- apply_matrix()
- pop_matrix()
- translate()
- scale()
- rotate()
- shear_x()
- shear_x()
- shear_y()
- rotate_x()
- rotate_y()
  
### Color

#### Settings

- background()
- clear()
- fill()
- no_fill()
- no_stroke()
- stroke()

#### Creating && Reading

- color()
- ch()
- bg()
- fg()
  
### Events

#### Keyboard

- key
- key_code
- key_typed()
  
#### Mouse

- mouse_clickd()
- mouseX
- mouseY
- pmouseX
- pmouseY
  
#### Cursor

- cursorX
- cursorY
- pcursorX
- pcursorY
- cursor_moved()

### Environment

- delay()
- cursor()
- window_width: the cols of the termianl
- window_height: the lines of the terminal
- window_resized()
- frame_rate()
- full_screen
- frame_count
- no_cursor()
- height
- size()
- width

### Constants

- HALF_PI
- PI
- QUARTER_PI
- TAU
- TWO_PI

### Math

CVector

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

### Typography

- text()
- text_width()
- text_align()
- text_leading()
- text_size()
- text_height()

### Image

- create_image()
- CImage
  
#### Loading & Displaying

- image()
- image_mode()
- load_image()
- no_tint()
- request_image()
- tint()
  
#### Textures

- texture()
- texture_mode()
- texture_wrap()
  
#### Pixels

- blend()
- copy()
- filter()
- get()
- load_pixels()
- pixels[]
- set()
- update_pixels()
