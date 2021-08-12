import charming as cm

cm.full_screen()
cm.no_cursor()

# basic colors
colors = [
    cm.RED,
    cm.BLACK,
    cm.CYAN,
    cm.YELLOW,
    cm.GREEN,
    cm.BLUE,
    cm.WHITE,
    cm.MAGENTA
]

cm.stroke_weight(1)
for i, c in enumerate(colors):
    x = 5
    y = 2
    cm.stroke("@", c, c)
    cm.point(i * 5 + x , y)

cm.run()
