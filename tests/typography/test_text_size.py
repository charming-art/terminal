import charming as cm

text = 'charming'

cm.full_screen()
cm.no_cursor()

cm.text(text, 0, 0)

cm.text_size(cm.BIG)
cm.text(text, 0, 2)

cm.text_size(cm.LARGE)
cm.text(text, 0, 8)

cm.run()