import charming as cm

cm.full_screen()
cm.no_cursor()
cm.no_stroke()

# Outer rect
cm.fill('O', cm.RED, cm.YELLOW)
cm.rect_mode(cm.CORNER) 
cm.rect(8, 4, 16, 8)

# Inner rect
cm.fill('V', cm.BLUE, cm.GREEN)
cm.rect_mode(cm.CORNERS)
cm.rect(8, 4, 16, 8)
cm.run()