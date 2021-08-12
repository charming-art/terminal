import charming as cm

cm.full_screen()
cm.no_cursor()
cm.quad(
    9, 0,  # point1
    27 + 5, 2,  # point2
    19, 12,  # point3
    9, 7  # point4
)
cm.run()
