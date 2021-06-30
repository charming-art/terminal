import charming as cm

text = 'ch'

cm.full_screen()
cm.no_cursor()
cm.translate(cm.get_width() / 2, cm.get_height() / 2)

cm.stroke('-')
cm.line(-cm.get_width() / 2, 0, cm.get_width() / 2, 0)
cm.text_size(cm.BIG)

# top
cm.text_align(cm.CENTER, align_y=cm.TOP)
cm.text(text, -20, 0)

# middle
cm.text_align(align_y=cm.MIDDLE)
cm.text(text, 0, 0)

# bottom
cm.text_align(align_y=cm.BOTTOM)
cm.text(text, 20, 0)


cm.run()
