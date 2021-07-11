import charming as cm

cm.full_screen()
cm.no_cursor()

cm.ellipse(5, 5, 10, 5)

with cm.open_context():
  cm.fill('+', cm.YELLOW, cm.CYAN)
  cm.stroke('O', cm.BLUE, cm.GREEN)
  cm.translate(15, 0)
  cm.ellipse(5, 5, 10, 5)

cm.ellipse(35, 5, 10, 5)

cm.run()
