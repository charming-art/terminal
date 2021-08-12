import charming as cm

cm.full_screen()
cm.color_mode(cm.RGB)
cm.no_cursor()

n = 7
cm.stroke_weight(1)

for i in range(n):
    c = cm.map(i, 0, n, 0, 255)
    cm.stroke("@", (c,), (c,))
    cm.point(i * 5 + 5, 2)

cm.run()
