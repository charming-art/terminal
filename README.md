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
- noLoop()
- loop()
- redraw()
- push()
- pop()

### Shape

- createShape()
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

- ellipseMode()
- rectMode()
- strokeWeight()

#### Vertex

- beginContour()
- beginShape()
- bezierVertex()
- curveVertex()
- endContour()
- endShape()
- quadraticVertex()
- vertex()

#### Curves

- bezier()
- bezierDetail()
- bezierPoint()
- bezierTangent()
- curve()
- curveDetail()
- curvePoint()
- curveTangent()
- curveTightness()

### Transform

- applyMatrix()
- popMatrix()
- translate()
- scale()
- rotate()
- shearX()
- shearX()
- shearY()
- rotateX()
- rotateY()
  
### Color

#### Settings

- background()
- clear()
- fill()
- noFill()
- noStroke()
- stroke()

#### Creating && Reading

- color()
- ch()
- bg()
- fg()
  
### Events

#### Keyboard

- key
- keyCode
- keyTyped()
  
#### Mouse

- mouseClickd()
- mouseX
- mouseY
- pmouseX
- pmouseY
  
#### Cursor

- cursorX
- cursorY
- pcursorX
- pcursorY
- cursorMoved()

### Environment

- delay()
- cursor()
- windowWidth: the cols of the termianl
- windowHeight: the lines of the terminal
- windowResized()
- frameRate()
- frameRate
- fullScreen
- frameCount
- noCursor()
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
- noiseDetail()
- noiseSeed()
- random()
- randomGaussian()
- randomSeed()

### Typography

- text()
- textWidth()
- textAlign()
- textLeading()
- textSize()
- textHeight()

### Image

- createImage()
- PImage
  
#### Loading & Displaying

- image()
- imageMode()
- loadImage()
- noTint()
- requestImage()
- tint()
  
#### Textures

- texture()
- textureMode()
- textureWrap()
  
#### Pixels

- blend()
- copy()
- filter()
- get()
- loadPixels()
- pixels[]
- set()
- updatePixels()
