import charming as cm

cm.full_screen()
cm.no_cursor()

for i in range(256):
    x = i % 32
    y = i // 32
    cm.stroke(' ', i, i)
    cm.point(x, y)

cm.run()
