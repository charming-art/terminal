import charming as cm

cm.full_screen()
cm.no_cursor()

cm.fill('@', cm.RED, cm.BLUE)
cm.rect(0, 0, 10, 5)

cm.fill('O', cm.YELLOW, cm.CYAN)
cm.rect(20, 0, 10, 5)

cm.run()