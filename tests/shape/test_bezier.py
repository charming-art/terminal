import charming as cm

cm.full_screen()
cm.no_cursor()

cm.stroke('@', cm.YELLOW, cm.RED)
cm.fill('+', cm.GREEN, cm.BLUE)

# only a bezier curve
with cm.open_context():
    cm.no_fill()
    cm.bezier(40, 5, 10, 10, 50, 20, 10, 30)

# a bezier curve with points
t = 0
cnt = 4
cm.translate(20, 0)
with cm.open_context():
    cm.no_fill()
    cm.bezier(40, 5, 10, 10, 50, 20, 10, 30)

    cm.stroke('a', cm.RED, cm.YELLOW)
    cm.stroke_weight(1)
    while t <= 1:
        x = cm.bezier_point(40, 10, 50, 10, t)
        y = cm.bezier_point(5, 10, 20, 30, t)
        cm.point(x, y)
        t += 1 / cnt

cm.run()
