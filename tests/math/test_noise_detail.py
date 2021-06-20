import charming as cm


cm.full_screen()
cm.color_mode(cm.RGB)
cm.no_cursor()

cm.background(' ')
for j in range(cm.get_height()):
    for i in range(cm.get_width()):
        mid = cm.ceil(cm.get_width() / 2)
        dist = cm.abs(i - mid)
        noise_scale = 0.02
        if i < mid:
            cm.noise_detail(2, 0.2)
        else:
            cm.noise_detail(8, 0.65)
        v = cm.noise(dist * noise_scale, j * noise_scale)
        c = cm.map(v, 0, 1, 0, 255)
        cm.stroke(' ', (c,), (c,))
        cm.point(i, j)

cm.run()
