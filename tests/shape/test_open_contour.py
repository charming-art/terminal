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