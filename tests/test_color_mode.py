import charming as app

app.full_screen()
# app.color_mode(app.HSB, 255, 100, 100)
# app.color_mode(app.RGB, 1000)
row = 34
start_x = int((app.get_width() - row) / 2)
start_y = int((app.get_height() - app.ceil(255 / 50)) / 2)
for i in range(255):
    x = i % row
    y = i / row
    app.stroke(' ', i, i)
    # app.stroke(' ', bg=(0, 0, i))
    # app.stroke(' ', bg=(i, 100, 100))
    app.point(start_x + x, start_y + y)

app.run()
