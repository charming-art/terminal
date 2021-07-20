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