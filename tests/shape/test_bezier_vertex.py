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