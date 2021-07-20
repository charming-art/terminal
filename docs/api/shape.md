# Shape

Methods for drawing shapes.

## 2D Primitives

Methods for drawing 2D basic shapes.

<a name="arc" href="#arc">#</a> cm.**arc**(*a*, *b*, *c*, *d*, *start*, *stop*, *mode=OPEN | CHORD | PIE*)

Draw an arc to the screen. If called with only x, y, w, h, start and stop, the arc will be drawn and filled as an open pie segment. If a mode parameter is provided, the arc will be filled like an open semi-circle (OPEN), a closed semi-circle (CHORD), or as a closed pie segment (PIE). The origin may be changed with the ellipseMode() function.The arc is always drawn clockwise from wherever start falls to wherever stop falls on the ellipse.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.arc(12, 5, 20, 10, 0, cm.PI + cm.QUARTER_PI, cm.OPEN)
cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_arc_open.png" width="100%"/>

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.arc(12, 5, 20, 10, 0, cm.PI + cm.QUARTER_PI, cm.PIE)
cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_arc_pie.png" width="100%"/>

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.arc(12, 5, 20, 10, 0, cm.PI + cm.QUARTER_PI, cm.CHORD)
cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_arc_chord.png" width="100%"/>

<a name="circle" href="#circle">#</a> cm.**circle**(*x*, *y*, *extend*)

Draws a circle to the screen. A circle is a simple closed shape. It is the set of all points in a plane that are at a given distance from a given point, the centre. This function is a special case of the ellipse() function, where the width and height of the ellipse are the same. Height and width of the ellipse correspond to the diameter of the circle. By default, the first two parameters set the location of the centre of the circle, the third sets the diameter of the circle.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.circle(12, 6, 10)
cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_circle.png" width="100%"/>

<a name="ellipse" href="#ellipse">#</a> cm.**ellipse**(*a*, *b*, *c*, *d*)

Draws an ellipse (oval) to the screen. By default, the first two parameters set the location of the center of the ellipse, and the third and fourth parameters set the shape's width and height. If no height is specified, the value of width is used for both the width and height. If a negative height or width is specified, the absolute value is taken.

An ellipse with equal width and height is a circle. The origin may be changed with the ellipse_mode() function.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.ellipse(12, 6, 20, 10)
cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_ellipse.png" width="100%"/>

<a name="line" href="#line">#</a> cm.**line**(*x1*, *y1*, *x2*, *y2*)

Draws a line (a direct path between two points) to the screen. This width can be modified by using the stroke_weight() function. A line cannot be filled, therefore the fill() function will not affect the color of a line. So to color a line, use the stroke() function.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.line(1, 1, 10, 10)
cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_line.png" width="100%"/>

<a name="point" href="#point">#</a> cm.**point**(*x*, *y*)

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.point(5, 5)
cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_point.png" width="100%"/>

<a name="quad" href="#quad">#</a> cm.**quad**(*x1*, *y1*, *x2*, *y2*, *x3*, *y3*, *x4*, *y4*)

Draws a quad on the canvas. A quad is a quadrilateral, a four sided polygon. It is similar to a rectangle, but the angles between its edges are not constrained to ninety degrees. The first pair of parameters (x1,y1) sets the first vertex and the subsequent pairs should proceed clockwise or counter-clockwise around the defined shape.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.quad(
    9, 0,  # point1
    27 + 5, 2,  # point2
    19, 12,  # point3
    9, 7  # point4
)
cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_quad.png" width="100%"/>

<a name="rect" href="#rect">#</a> cm.**rect**(*a*, *b*, *c*, *d*)

Draws a rectangle on the canvas. A rectangle is a four-sided closed shape with every angle at ninety degrees. By default, the first two parameters set the location of the upper-left corner, the third sets the width, and the fourth sets the height. The way these parameters are interpreted, may be changed with the rect_mode() function.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.rect(1, 1, 10, 10)
cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_rect.png" width="100%"/>

<a name="square" href="#square">#</a> cm.**square**(*x*, *y*, *extend*)

Draws a square to the screen. A square is a four-sided shape with every angle at ninety degrees, and equal side size. This function is a special case of the rect() function, where the width and height are the same, and the parameter is called "s" for side size. By default, the first two parameters set the location of the upper-left corner, the third sets the side size of the square. The way these parameters are interpreted, may be changed with the rect_mode() function.


```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.square(1, 1, 10)
cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_square.png" width="100%"/>

<a name="triangle" href="#triangle">#</a> cm.**square**(*x1*, *y1*, *x2*, *y2*, *x3*, *y3*)

Draws a triangle to the canvas. A triangle is a plane created by connecting three points. The first two arguments specify the first point, the middle two arguments specify the second point, and the last two arguments specify the third point.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.triangle(
    6, 0,  # point1
    12, 6,  # point2
    0, 6 # point3
)
cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_triangle.png" width="100%"/>

## Attributes

Methods for setting drawing attributes.

<a name="ellipse_mode" href="#ellipse_mode">#</a> cm.**ellipse_mode**(*mode=CENTER | RADIUS | CORNER | CORNERS*)

Modifies the location from which ellipses are drawn by changing the way in which parameters given to ellipse(), circle() and arc() are interpreted.

The default mode is CENTER, in which the first two parameters are interpreted as the shape's center point's x and y coordinates respectively, while the third and fourth parameters are its width and height.

ellipse_mode(RADIUS) also uses the first two parameters as the shape's center point's x and y coordinates, but uses the third and fourth parameters to specify half of the shape's width and height.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.no_stroke()

# Outer  ellipse
cm.fill('O', cm.RED, cm.YELLOW)
cm.ellipse_mode(cm.RADIUS) 
cm.ellipse(12, 6, 20, 10)

# Inner ellipse
cm.fill('V', cm.BLUE, cm.GREEN)
cm.ellipse_mode(cm.CENTER)
cm.ellipse(12, 6, 20, 10)
cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_ellipse_mode_center.png" width="100%"/>

ellipse_mode(CORNER) interprets the first two parameters as the upper-left corner of the shape, while the third and fourth parameters are its width and height.

ellipse_mode(CORNERS) interprets the first two parameters as the location of one corner of the ellipse's bounding box, and the third and fourth parameters as the location of the opposite corner.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.no_stroke()

# Outer  ellipse
cm.fill('O', cm.RED, cm.YELLOW)
cm.ellipse_mode(cm.CORNER) 
cm.ellipse(8, 4, 16, 8)

# Inner ellipse
cm.fill('V', cm.BLUE, cm.GREEN)
cm.ellipse_mode(cm.CORNERS)
cm.ellipse(8, 4, 16, 8)
cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_ellipse_mode_corner.png" width="100%"/>

<a name="rect_mode" href="#rect_mode">#</a> cm.**rect_mode**(*mode=CENTER | RADIUS | CORNER | CORNERS*)

Modifies the location from which rectangles are drawn by changing the way in which parameters given to rect() are interpreted.

The default mode is CORNER, which interprets the first two parameters as the upper-left corner of the shape, while the third and fourth parameters are its width and height.

rect_mode(CORNERS) interprets the first two parameters as the location of one of the corners, and the third and fourth parameters as the location of the diagonally opposite corner. Note, the rectangle is drawn between the coordinates, so it is not necessary that the first corner be the upper left corner.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.no_stroke()

# Outer rect
cm.fill('O', cm.RED, cm.YELLOW)
cm.rect_mode(cm.CORNER) 
cm.rect(8, 4, 16, 8)

# Inner rect
cm.fill('V', cm.BLUE, cm.GREEN)
cm.rect_mode(cm.CORNERS)
cm.rect(8, 4, 16, 8)
cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_rect_mode_corner.png" width="100%"/>

rect_mode(CENTER) interprets the first two parameters as the shape's center point, while the third and fourth parameters are its width and height.

rect_mode(RADIUS) also uses the first two parameters as the shape's center point, but uses the third and fourth parameters to specify half of the shape's width and height respectively.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.no_stroke()

# Outer  rect
cm.fill('O', cm.RED, cm.YELLOW)
cm.rect_mode(cm.RADIUS) 
cm.rect(12, 6, 10, 5)

# Inner rect
cm.fill('V', cm.BLUE, cm.GREEN)
cm.rect_mode(cm.CENTER)
cm.rect(12, 6, 10, 5)
cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_rect_mode_center.png" width="100%"/>

<a name="stroke_weight" href="#stroke_weight">#</a> cm.**stroke_weight**(*weight=0*)

Sets the width of the stroke used for lines, points and the border around shapes. All widths are set in units of cells.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

cm.stroke_weight(0) # Default
cm.stroke('O')
cm.line(3, 0, 25, 0)

cm.stroke('A')
cm.stroke_weight(1) # Thicker
cm.line(3, 3, 25, 3)

cm.stroke('X')
cm.stroke_weight(2) # Beastly
cm.line(3, 8, 25, 8)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_stroke_weight.png" width="100%"/>

## Vertex

Methods for drawing custom shapes.

<a name="begin_shape" href="#begin_shape">#</a> cm.**begin_shape**(*primitive_type=POLYGON | POINTS | LINES | TRIANGLES | TRIANGLE_STRIP | TRIANGLE_FAN | QUADS | QUAD_STRIP*)

Using the begin_shape() and end_shape() functions allow creating more complex forms. begin_shape() begins recording vertices for a shape and end_shape() stops recording. The value of the kind parameter tells it which types of shapes to create from the provided vertices. With no mode specified, the shape can be any irregular polygon.

```py
import charming as cm

# environment
cm.full_screen()
cm.no_cursor()

# styles
cm.fill('*', cm.YELLOW, cm.RED)
cm.stroke('@', cm.GREEN, cm.BLUE)

# custom shapes
cm.begin_shape()
cm.vertex(1, 1)
cm.vertex(6, 1)
cm.vertex(6, 6)
cm.vertex(1, 6)
cm.end_shape(close_mode=cm.CLOSE)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_polygon.png" width="100%"/>

```py
import charming as cm

# environment
cm.full_screen()
cm.no_cursor()

# styles
cm.fill('*', cm.YELLOW, cm.RED)
cm.stroke('@', cm.GREEN, cm.BLUE)

# custom shapes
cm.begin_shape(cm.LINES)
cm.vertex(1, 1)
cm.vertex(6, 1)
cm.vertex(6, 6)
cm.vertex(1, 6)
cm.end_shape(close_mode=cm.CLOSE)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_lines.png" width="100%"/>

```py
import charming as cm

# environment
cm.full_screen()
cm.no_cursor()

# styles
cm.fill('*', cm.YELLOW, cm.RED)
cm.stroke('@', cm.GREEN, cm.BLUE)

# custom shapes
cm.begin_shape(cm.POINTS)
cm.vertex(1, 1)
cm.vertex(6, 1)
cm.vertex(6, 6)
cm.vertex(1, 6)
cm.end_shape(close_mode=cm.CLOSE)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_points.png" width="100%"/>

```py
import charming as cm

# environment
cm.full_screen()
cm.no_cursor()

# styles
cm.fill('*', cm.YELLOW, cm.RED)
cm.stroke('@', cm.GREEN, cm.BLUE)

# custom shapes
cm.begin_shape(cm.TRIANGLES)
cm.vertex(1, 6)
cm.vertex(5, 1)
cm.vertex(10, 6)
cm.vertex(15, 1)
cm.vertex(20, 6)
cm.vertex(25, 1)
cm.end_shape(close_mode=cm.CLOSE)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_triangles.png" width="100%"/>

```py
import charming as cm

# environment
cm.full_screen()
cm.no_cursor()

# styles
cm.fill('*', cm.YELLOW, cm.RED)
cm.stroke('@', cm.GREEN, cm.BLUE)

# custom shapes
cm.begin_shape(cm.TRIANGLE_STRIP)
cm.vertex(1, 6)
cm.vertex(5, 1)
cm.vertex(10, 6)
cm.vertex(15, 1)
cm.vertex(20, 6)
cm.vertex(25, 1)
cm.vertex(30, 6)
cm.end_shape(close_mode=cm.CLOSE)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_triangle_strip.png" width="100%"/>

```py
import charming as cm

# environment
cm.full_screen()
cm.no_cursor()

# styles
cm.fill('*', cm.YELLOW, cm.RED)
cm.stroke('@', cm.GREEN, cm.BLUE)

# custom shapes
cm.begin_shape(cm.TRIANGLE_FAN)
cm.vertex(11, 6)
cm.vertex(11, 1)
cm.vertex(21, 6)
cm.vertex(11, 11)
cm.vertex(1, 6)
cm.vertex(11, 1)
cm.end_shape(close_mode=cm.CLOSE)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_triangle_fan.png" width="100%"/>

```py
import charming as cm

# environment
cm.full_screen()
cm.no_cursor()

# styles
cm.fill('*', cm.YELLOW, cm.RED)
cm.stroke('@', cm.GREEN, cm.BLUE)

# custom shapes
cm.begin_shape(cm.QUADS)
cm.vertex(1, 1)
cm.vertex(1, 6)
cm.vertex(6, 6)
cm.vertex(6, 1)
cm.vertex(11, 1)
cm.vertex(11, 6)
cm.vertex(16, 6)
cm.vertex(16, 1)
cm.end_shape(close_mode=cm.CLOSE)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_quads.png" width="100%"/>

```py
import charming as cm

# environment
cm.full_screen()
cm.no_cursor()

# styles
cm.fill('*', cm.YELLOW, cm.RED)
cm.stroke('@', cm.GREEN, cm.BLUE)

# custom shapes
cm.begin_shape(cm.QUAD_STRIP)
cm.vertex(1, 1)
cm.vertex(1, 6)
cm.vertex(6, 1)
cm.vertex(6, 6)
cm.vertex(11, 1)
cm.vertex(11, 6)
cm.vertex(16, 1)
cm.vertex(16, 6)
cm.end_shape(close_mode=cm.CLOSE)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_quad_strip.png" width="100%"/>

<a name="end_shape" href="#end_shape">#</a> cm.**end_shape**(*mode=OPEN | CLOSE*)

The end_shape() function is the companion to begin_shape() and may only be called after begin_shape(). When endShape() is called, all of image data defined since the previous call to begin_shape() is written into the image buffer. The constant CLOSE as the value for the MODE parameter to close the shape (to connect the beginning and the end).

```py
import charming as cm

# environment
cm.full_screen()
cm.no_cursor()

# styles
cm.fill('*', cm.YELLOW, cm.RED)
cm.stroke('@', cm.GREEN, cm.BLUE)

# custom shapes
cm.begin_shape()
cm.vertex(1, 1)
cm.vertex(6, 1)
cm.vertex(1, 6)
cm.end_shape()

cm.begin_shape()
cm.vertex(8, 1)
cm.vertex(13, 1)
cm.vertex(8, 6)
cm.end_shape(cm.CLOSE)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_end_shape.png" width="100%"/>

<a name="vertex" href="#vertex">#</a> cm.**vertex**(*x*, *y*)

All shapes are constructed by connecting a series of vertices. vertex() is used to specify the vertex coordinates for points, lines, triangles, quads, and polygons. It is used exclusively within the begin_shape() and end_shape() functions.

```py
import charming as cm

# environment
cm.full_screen()
cm.no_cursor()

# styles
cm.fill('*', cm.YELLOW, cm.RED)
cm.stroke('@', cm.GREEN, cm.BLUE)

# custom shapes
cm.begin_shape()
cm.vertex(1, 1)
cm.vertex(6, 1)
cm.vertex(6, 6)
cm.vertex(1, 6)
cm.end_shape(close_mode=cm.CLOSE)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_begin_shape_polygon.png" width="100%"/>

<a name="open_shape" href="#open_shape">#</a> cm.**open_shape**(*primitive_type=POLYGON | POINTS | LINES | TRIANGLES | TRIANGLE_STRIP | TRIANGLE_FAN, mode=OPEN | CLOSE*)

The syntactic sugar for begin_shape() and end_shape().

```py
import charming as cm

# environment
cm.full_screen()
cm.no_cursor()

# styles
cm.fill('*', cm.YELLOW, cm.RED)
cm.stroke('@', cm.GREEN, cm.BLUE)

with cm.open_shape(cm.LINES, cm.CLOSE):
    cm.vertex(1, 1)
    cm.vertex(6, 1)
    cm.vertex(6, 6)
    cm.vertex(1, 6)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_open_shape.png" width="100%"/>

<a name="begin_contour" href="#begin_contour">#</a> cm.**begin_contour**()
<a name="end_contour" href="#end_contour">#</a> cm.**end_contour**()

Use the begin_contour() and end_contour() functions to create negative shapes within shapes such as the center of the letter 'O'. beginContour() begins recording vertices for the shape and endContour() stops recording. The vertices that define a negative shape must "wind" in the opposite direction from the exterior shape. First draw vertices for the exterior clockwise order, then for internal shapes, draw vertices shape in counter-clockwise.

These functions can only be used within a begin_shape()/end_shape() pair and transformations such as translate(), rotate(), and scale() do not work within a begin_contour()/end_contour() pair. It is also not possible to use other shapes, such as ellipse() or rect() within.

```py
import charming as cm

# environment
cm.full_screen()
cm.no_cursor()

# styles
cm.fill('*', cm.YELLOW, cm.RED)
cm.stroke('@', cm.GREEN, cm.BLUE)

# Outer shape
cm.begin_shape()

cm.vertex(0, 0)
cm.vertex(15, 0)
cm.vertex(15, 15)
cm.vertex(0, 15)

# Inner shape
cm.begin_contour()
cm.vertex(5, 5)
cm.vertex(5, 10)
cm.vertex(10, 10)
cm.vertex(10, 5)
cm.end_contour()

cm.end_shape(cm.CLOSE)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_contour.png" width="100%"/>

<a name="open_contour" href="#open_contour">#</a> cm.**open_contour**()

The syntactic sugar for begin_contour() and end_contour().

```py
import charming as cm

# environment
cm.full_screen()
cm.no_cursor()

# styles
cm.fill('*', cm.YELLOW, cm.RED)
cm.stroke('@', cm.GREEN, cm.BLUE)

# Shapes
cm.begin_shape()
with cm.open_shape(close_mode=cm.CLOSE):
  cm.vertex(0, 0)
  cm.vertex(15, 0)
  cm.vertex(15, 15)
  cm.vertex(0, 15)
  with cm.open_contour():
    cm.vertex(5, 5)
    cm.vertex(5, 10)
    cm.vertex(10, 10)
    cm.vertex(10, 5)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_open_contour.png" width="100%"/>

<a name="bezier_vertex" href="#bezier_vertex">#</a> cm.**bezier_vertex**(*x1*, *y1*, *x2*, *y2*, *x3*, *y3*)

Specifies vertex coordinates for Bezier curves. Each call to bezier_vertex() defines the position of two control points and one anchor point of a Bezier curve, adding a new segment to a line or shape.

The first time bezier_vertex() is used within a begin_shape() call, it must be prefaced with a call to vertex() to set the first anchor point. This function must be used between begin_shape() and end_shape() and only when there is no MODE or POINTS parameter specified to begin_shape().

```py
import charming as cm

# environment
cm.full_screen()
cm.no_cursor()

# styles
cm.fill('*', cm.YELLOW, cm.RED)
cm.stroke('@', cm.GREEN, cm.BLUE)

# custom curve
with cm.open_shape():
    cm.vertex(30, 5)
    cm.bezier_vertex(80, 0, 80, 35, 30, 35)
    cm.bezier_vertex(50, 30, 60, 25, 30, 5)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_bezier_vertex.png" width="100%"/>

<a name="curve_vertex" href="#curve_vertex">#</a> cm.**bezier_vertex**(*x*, *y*)

Specifies vertex coordinates for curves. This function may only be used between begin_shape() and end_shape() and only when there is no MODE parameter specified to begin_shape().

The first and last points in a series of curve_vertex() lines will be used to guide the beginning and end of a the curve. A minimum of four points is required to draw a tiny curve between the second and third points. Adding a fifth point with curve_vertex() will draw the curve between the second, third, and fourth points. The curve_vertex() function is an implementation of Catmull-Rom splines.

```py
import charming as cm

# environment
cm.full_screen()
cm.no_cursor()

# styles
cm.fill('*', cm.YELLOW, cm.RED)
cm.stroke('@', cm.GREEN, cm.BLUE)

# custom curve
with cm.open_shape():
    cm.curve_vertex(44, 21)
    cm.curve_vertex(44, 21)
    cm.curve_vertex(48, 9)
    cm.curve_vertex(21, 7)
    cm.curve_vertex(2, 30)
    cm.curve_vertex(2, 30)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_curve_vertex.png" width="100%"/>

## Curves

Methods for drawing curves.

<a name="bezier" href="#bezier">#</a> cm.**vertex**(*x1*, *y1*, *x2*, *y2*, *x3*, *y3*, *x4*, *y4*)

<a name="bezier_point" href="#bezier_point">#</a> cm.**bezier_point**(*n1*, *n2*, *n3*, *n4*, *t*)

<a name="bezier_tangent" href="#bezier_tangent">#</a> cm.**bezier_tangent**(*n1*, *n2*, *n3*, *n4*, *t*)

<a name="curve" href="#curve">#</a> cm.**curve**(*x1*, *y1*, *x2*, *y2*, *x3*, *y3*, *x4*, *y4*)

<a name="curve_point" href="#curve_point">#</a> cm.**curve_point**(*n1*, *n2*, *n3*, *n4*, *t*)

<a name="curve_tangent" href="#curve_tangent">#</a> cm.**curve_tangent**(*n1*, *n2*, *n3*, *n4*, *t*)

<a name="curve_tightness" href="#curve_tightness">#</a> cm.**curve_tangent**(*v*)