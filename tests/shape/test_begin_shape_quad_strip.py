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