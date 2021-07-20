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