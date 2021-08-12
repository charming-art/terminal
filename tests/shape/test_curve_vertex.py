import charming as cm

# environment
cm.full_screen()
cm.no_cursor()

# styles
cm.fill('*', cm.YELLOW, cm.RED)
cm.stroke('@', cm.GREEN, cm.BLUE)

# custom curve
with cm.open_shape():
    cm.curve_vertex(44, 21)
    cm.curve_vertex(44, 21)
    cm.curve_vertex(48, 9)
    cm.curve_vertex(21, 7)
    cm.curve_vertex(2, 30)
    cm.curve_vertex(2, 30)

cm.run()
