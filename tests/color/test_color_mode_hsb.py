import charming as cm

cm.full_screen()
cm.color_mode(cm.HSB)
cm.no_cursor()

# rainbows
w = 30
h = 360 / w

for hue in range(360):
    i = hue % w
    j = hue // w
    cm.stroke(" ", (hue, 100, 100), (hue, 100, 100))
    cm.point(i, j)

cm.run()