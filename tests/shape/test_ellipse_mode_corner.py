import charming as cm

cm.full_screen()
cm.no_cursor()
cm.no_stroke()

# Outer  ellipse
cm.fill('O', cm.RED, cm.YELLOW)
cm.ellipse_mode(cm.CORNER) 
cm.ellipse(8, 4, 16, 8)

# Inner ellipse
cm.fill('V', cm.BLUE, cm.GREEN)
cm.ellipse_mode(cm.CORNERS)
cm.ellipse(8, 4, 16, 8)
cm.run()
