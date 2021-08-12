import charming as cm

cm.full_screen()
cm.no_cursor()

cm.stroke('@', cm.YELLOW, cm.RED)
cm.fill('+', cm.GREEN, cm.BLUE)

# A curve with some points
with cm.open_context():
    cm.no_fill()
    cm.curve(-55, 26, 13, 24, 13, 11, -45, 25)

    t = 0
    cnt = 3
    cm.stroke('p', cm.CYAN, cm.RED)
    cm.stroke_weight(1)
    while t <= 1:
        x = cm.curve_point(-55, 13, 13, -45, t)
        y = cm.curve_point(26, 24, 11, 25, t)
        cm.point(x, y)
        t += 1 / cnt


cm.run()
