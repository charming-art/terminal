import charming as cm

cm.full_screen()
cm.no_cursor()

x = cm.get_width() / 2
y = cm.get_height() / 2
r = cm.get_height() * 0.8

cm.arc(x, y, r * 2, r, 0, cm.QUARTER_PI, cm.PIE)

cm.run()