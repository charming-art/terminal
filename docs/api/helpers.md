# Helpers

<a name="print" href="#print">#</a> cm.**print**(*\*args*, *\*\*kw*) : any

Print output to file to debug.

```py
import charming as app

app.print(1)
app.print([1, 2, 3])
app.print(2, 3, {'hello': 1}, test="test")
```

<a name="check_params" href="#check_params">#</a> cm.**check_params**()

Checks the type of params to output the potential error.

```py
import charming as cm

cm.full_screen()
cm.check_params()

cm.arc(0, 0, 0, 0, 'a', 'b')
cm.circle(0, 0, 'c')
cm.ellipse(0, 0, 'c', 'c')
cm.line(0, 0, 'c', 'c')
cm.point('c', 1)
cm.quad(0, 0, 0, 0, 0, 'c', 'c', 0)
cm.rect(0, 0, 0, 'c')
cm.square(0, 0, 'c')
cm.triangle(0, 0, 0, 0,  0, 'c')
cm.ellipse_mode('c')
cm.rect_mode('c')
cm.stroke_weight('c')
cm.begin_shape('c')
cm.bezier_vertex(0, 0, 0, 0, 0, 'c')
cm.curve_vertex(0, 'c')
cm.end_shape('up')
cm.vertex(0, 'c')
cm.open_shape('c', 'c')
cm.bezier(0, 0, 0, 0, 0, 0, 0, 'c')
cm.bezier_point(0, 0, 0, 'c', 1)
cm.bezier_tangent(0, 0, 0, 0, 'c')
cm.curve(0, 0, 0, 0, 0, 0, 0, 'c')
cm.curve_point(0, 0, 0, 0, 'c')
cm.curve_tangent(0, 0, 0, 0, 'c')
cm.curve_tightness('c')
cm.translate(0, 'c')
cm.scale('0')
cm.shear_x('0')
cm.shear_y('0')
cm.image('a', 0, 0, 0, 0)
cm.image_mode('c')
cm.load_image(0)
cm.color_mode(cm.RGB)
cm.tint(' ', (1, 0))
cm.text(0, 0, 0)
cm.text_width(0)
cm.text_height(0)
cm.text_size(0.0)
cm.text_font(0)
cm.set_cursor('c', 0)
cm.color_mode(cm.RGB)
cm.background('c', (0, 0, ))
cm.fill('c', (0, 0, ))
cm.stroke('c', (0, ))
c = cm.CColor('c', (1,))
cm.lerp_color(c, c, 0.5)

cm.run()
```
  