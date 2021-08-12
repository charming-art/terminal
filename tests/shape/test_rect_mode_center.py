import charming as cm

cm.full_screen()
cm.no_cursor()
cm.no_stroke()

# Outer  rect
cm.fill('O', cm.RED, cm.YELLOW)
cm.rect_mode(cm.RADIUS) 
cm.rect(12, 6, 10, 5)

# Inner rect
cm.fill('V', cm.BLUE, cm.GREEN)
cm.rect_mode(cm.CENTER)
cm.rect(12, 6, 10, 5)
cm.run()