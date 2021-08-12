import charming as cm

cm.full_screen()
cm.no_cursor()

start = cm.CColor('a', cm.BLUE, cm.RED)  # start color
end = cm.CColor('z', cm.GREEN, cm.YELLOW)  # end color

cm.stroke_weight(1)
n = 10
for i in range(n):
    t = i / n
    c = cm.lerp_color(start, end, t)
    cm.stroke(c)
    cm.point(i * 5 + 5, 2)

cm.run()
