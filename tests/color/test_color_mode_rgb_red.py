import charming as cm

cm.full_screen()
cm.no_cursor()
cm.color_mode(cm.RGB)

n = 7
cm.stroke_weight(1)

for i in range(n):
    c = cm.map(i, 0, n, 0, 255)
    cm.stroke(" ", (c, 0, 0), (c, 0, 0))
    cm.point(i * 5 + 5, 2)

cm.run()
