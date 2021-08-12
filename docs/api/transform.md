# Transform

<a name="translate" href="#translate">#</a> cm.**translate**(*tx*, *ty*)

Specifies an amount to displace objects within the display window. The x parameter specifies left/right translation, the y parameter specifies up/down translation.

Transformations are cumulative and apply to everything that happens after and subsequent calls to the function accumulates the effect. For example, calling translate(50, 0) and then translate(20, 0) is the same as translate(70, 0). If translate() is called within draw(), the transformation is reset when the loop begins again. This function can be further controlled by using push() and pop().

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

cm.rect(0, 0, 5, 5)
cm.translate(10, 10)
cm.rect(0, 0, 5, 5)
cm.translate(10, 10)
cm.rect(0, 0, 5, 5)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_translate.png" />

<a name="scale" href="#scale">#</a> cm.**scale**(*sx*[, *sy*])

Increases or decreases the size of a shape by expanding or contracting vertices. Objects always scale from their relative origin to the coordinate system. Scale values are specified as decimal percentages. For example, the function call scale(2.0) increases the dimension of a shape by 200%.

Transformations apply to everything that happens after and subsequent calls to the function multiply the effect. For example, calling scale(2.0) and then scale(1.5) is the same as scale(3.0). If scale() is called within draw(), the transformation is reset when the loop begins again.

This function can be further controlled with push() and pop().

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

cm.stroke('%')
cm.rect(3, 2, 10, 6)
cm.scale(2, 2)
cm.rect(3, 2, 10, 6)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_scale.png" />

<a name="rotate" href="#rotate">#</a> cm.**rotate**(*x*)

Rotates a shape by the amount specified by the angle parameter.

Objects are always rotated around their relative position to the origin and positive numbers rotate objects in a clockwise direction. Transformations apply to everything that happens after and subsequent calls to the function accumulates the effect. For example, calling rotate(HALF_PI) and then rotate(HALF_PI) is the same as rotate(PI). All transformations are reset when draw() begins again.

Technically, rotate() multiplies the current transformation matrix by a rotation matrix. This function can be further controlled by the push() and pop().

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

cm.stroke('%')
cm.translate(cm.get_width() / 2, cm.get_height() / 2)
cm.rotate(cm.PI / 3.0)
cm.rect(-5, -5, 10, 10)


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_rotate.png" />

<a name="shear_x" href="#shear_x">#</a> cm.**shear_x**(*x*)

Shears a shape around the x-axis by the amount specified by the angle parameter.

Objects are always sheared around their relative position to the origin and positive numbers shear objects in a clockwise direction.

Transformations apply to everything that happens after and subsequent calls to the function accumulates the effect. For example, calling shear_x(PI/2) and then shear_y(PI/2) is the same as shear_x(PI). If shear_x() is called within the draw(), the transformation is reset when the loop begins again.

Technically, shear_x() multiplies the current transformation matrix by a rotation matrix. This function can be further controlled by the push() and pop() functions.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

cm.stroke('%')
cm.translate(cm.get_width() / 2, cm.get_height() / 2)
cm.shear_x(cm.PI / 3.0)
cm.rect(-5, -5, 10, 10)


cm.run()

```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_shear_x.png" />

<a name="shear_y" href="#shear_y">#</a> cm.**shear_y**(*x*)

Shears a shape around the y-axis the amount specified by the angle parameter. Objects are always sheared around their relative position to the origin and positive numbers shear objects in a clockwise direction.

Transformations apply to everything that happens after and subsequent calls to the function accumulates the effect. For example, calling shear_y(PI/2) and then shear_y(PI/2) is the same as shear_y(PI). If shear_y() is called within the draw(), the transformation is reset when the loop begins again.

Technically, shear_y() multiplies the current transformation matrix by a rotation matrix. This function can be further controlled by the push() and pop() functions.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

cm.stroke('%')
cm.translate(cm.get_width() / 2, cm.get_height() / 2)
cm.shear_y(cm.PI / 3.0)
cm.rect(-5, -5, 10, 10)


cm.run()

```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_shear_y.png" />