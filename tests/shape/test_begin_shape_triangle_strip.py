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