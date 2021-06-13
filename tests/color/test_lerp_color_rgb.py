import charming as cm

cm.full_screen()
cm.no_cursor()
cm.color_mode(cm.RGB)

start = cm.CColor('a', (0,), (255, 0, 0))
end = cm.CColor('z', (255, 255, 0), (0,))
n = 10

for i in range(n):
    t = i / n
    c = cm.lerp_color(start, end, t)
    cm.stroke_weight(1)
    cm.stroke(c)
    cm.point(i * 5 + 5, 2)

cm.run()