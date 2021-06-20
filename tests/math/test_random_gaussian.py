import charming as cm

cm.full_screen()
cm.no_cursor()

for y in range(cm.get_height()):
  mid = cm.get_width() / 2
  x = cm.random_gaussian(mid, 40)
  cm.stroke('$')
  cm.line(mid, y, x, y)

cm.run()