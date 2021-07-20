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
