import charming as cm

cm.full_screen()
cm.no_cursor()

cm.stroke_weight(0) # Default
cm.stroke('O')
cm.line(3, 0, 25, 0)

cm.stroke('A')
cm.stroke_weight(1) # Thicker
cm.line(3, 3, 25, 3)

cm.stroke('X')
cm.stroke_weight(2) # Beastly
cm.line(3, 8, 25, 8)

cm.run()