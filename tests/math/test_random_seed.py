import charming as cm

cm.full_screen()
cm.no_cursor()
cm.color_mode(cm.RGB)

cm.random_seed(99)
for i in range(cm.get_width()):
    r = cm.random(0, 255)
    cm.stroke(' ', (r,), (r, ))
    cm.line(i, 0, i, cm.get_height())

cm.run()
