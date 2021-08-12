import charming as cm

cm.full_screen()
cm.no_cursor()
cm.text_size(cm.BIG)

font_list = cm.get_font_list()
text = 'charming'

th = cm.text_height(text)
cm.text(text, 0, 0)

cm.text_font(font_list[0])
th1 = cm.text_height(text)
cm.text(text, 0, th)

cm.text_font(font_list[1])
cm.text(text, 0, th + th1)

cm.run()
