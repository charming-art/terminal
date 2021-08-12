import charming as cm

cm.full_screen()
cm.no_cursor()

cm.stroke('%')
cm.translate(cm.get_width() / 2, cm.get_height() / 2)
cm.shear_y(cm.PI / 3.0)
cm.rect(-5, -5, 10, 10)


cm.run()
