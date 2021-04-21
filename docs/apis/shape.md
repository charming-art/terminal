# Shape

## 2D Primitives

- `arc(a, b, c, d, start, stop, mode=OPEN | CHORD | PIE)`
- `circle(x, y, extend)`
- `ellipse(a, b, c, d)`
- `line(x1, y1, x2, y2)`
- `point(x, y)`
- `quad(x1, y1, x2, y2, x3, y3, x4, y4)`
- `rect(a, b, c, d)`
- `square(x, y, extend)`
- `triangle(x1, y1, x2, y2, x3, y3)`
  
## Attributes

- `ellipse_mode(mode=CENTER | RADIUS | CORNER | CORNERS)`
- `rect_mode(mode=CORNER | CORNERS | CENTER | RADIUS)`
- `stroke_weight(weight=0)`

## Vertex

- `begin_contour()`
- `begin_shape(primitive_type=POLYGON | POINTS | LINES | TRIANGLES | TRIANGLE_STRIP | TRIANGLE_FAN | QUADS | QUAD_STRIP)`
- `bezier_vertex(x2, y2, x3, y3, x4, y4)`
- `curve_vertex(x, y)`
- `end_contour()`
- `end_shape(mode=OPEN | CLOSE)`
- `vertex(x, y)`
- `open_shape(primitive_type=POLYGON | POINTS | LINES | TRIANGLES | TRIANGLE_STRIP | TRIANGLE_FAN, mode=OPEN | CLOSE)`
- `open_contour()`
  
## Curves

- `bezier(x1, y1, x2, y2, x3, y3, x4, y4)`
- `bezier_point(n1, n2, n3, n4, t)`
- `bezier_tangent(n1, n2, n3, n4, t)`
- `curve(x1, y1, x2, y2, x3, y3, x4, y4)`
- `curve_point(n1, n2, n3, n4, t)`
- `curve_tangent(n1, n2, n3, n4, t)`
- `curve_tightness(v)`

## Examples

- [2d Primitives](https://github.com/charming-art/charming/blob/master/tests/test_shape_primitives.py)
- [Vertex](https://github.com/charming-art/charming/blob/master/tests/test_shape_vertex.py)
- [Curve](https://github.com/charming-art/charming/blob/master/tests/test_shape_curve.py)
- [Bezier](https://github.com/charming-art/charming/blob/master/tests/test_shape_bezier.py)
- [Attributes](https://github.com/charming-art/charming/blob/master/tests/test_shape_attributes.py)