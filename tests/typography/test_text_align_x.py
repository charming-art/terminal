import charming as cm

text = 'charming'

cm.full_screen()
cm.no_cursor()
cm.translate(cm.get_width() / 2, cm.get_height() / 2)

cm.stroke('|')
cm.line(0, -cm.get_height() / 2, 0, cm.get_height() / 2)

# left
cm.text_align(cm.LEFT)
cm.text(text, 0, -5)

# center
cm.text_align(cm.CENTER)
cm.text(text, 0, 0)

# right
cm.text_align(cm.RIGHT)
cm.text(text, 0, 5)


cm.run()
