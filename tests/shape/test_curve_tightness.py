import charming as cm

cm.full_screen()
cm.no_cursor()

cm.stroke('@', cm.YELLOW, cm.RED)
cm.fill('+', cm.GREEN, cm.BLUE)

# A curve with tightness of 1
with cm.open_context():
    cm.curve_tightness(1)
    cm.no_fill()
    cm.curve(-55, 26, 13, 24, 13, 11, -45, 25)

# A curve with tightness of 0
with cm.open_context():
    cm.translate(20, 0)
    cm.curve_tightness(0)  # default
    cm.no_fill()
    cm.curve(-55, 26, 13, 24, 13, 11, -45, 25)

cm.run()
