import charming as cm

cm.full_screen()
cm.no_cursor()

cm.rect(0, 0, 5, 5)
cm.translate(10, 10)
cm.rect(0, 0, 5, 5)
cm.translate(10, 10)
cm.rect(0, 0, 5, 5)

cm.run()
