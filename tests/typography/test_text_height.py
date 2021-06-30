import charming as cm

cm.full_screen()
cm.no_cursor()

text = 'C'
height = cm.get_height()
width = cm.get_width()

cm.text(text, 0, (height - cm.text_height(text)) / 2)

cm.text_size(cm.BIG)
cm.text(text, 10, (height - cm.text_height(text)) / 2)

cm.text_size(cm.LARGE)
cm.text(text, 20, (height - cm.text_height(text)) / 2)

cm.run()
