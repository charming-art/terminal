import charming as cm

cm.full_screen()
cm.no_cursor()

text = 'charming'
width = cm.get_width()

th1 = cm.text_height(text)
cm.text(text, (width - cm.text_width(text)) / 2, 0)

cm.text_size(cm.BIG)
th2 = cm.text_height(text)
cm.text(text, (width - cm.text_width(text)) / 2, th1)

cm.text_size(cm.LARGE)
cm.text(text, (width - cm.text_width(text)) / 2, th1 + th2)

cm.run()
