import charming as cm

cm.full_screen()
cm.no_cursor()
cm.no_stroke()

# Outer  ellipse
cm.fill('O', cm.RED, cm.YELLOW)
cm.ellipse_mode(cm.RADIUS) 
cm.ellipse(12, 6, 12, 6)

# Inner ellipse
cm.fill('V', cm.BLUE, cm.GREEN)
cm.ellipse_mode(cm.CENTER)
cm.ellipse(12, 6, 12, 6)
cm.run()
