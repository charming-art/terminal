import charming as app

app.full_screen()
row = 34
start_x = int((app.get_width() - row) / 2)
start_y = int((app.get_height() - app.ceil(255 / 50)) / 2)
app.log([app.get_width() / 2, app.get_height() / 2])
for i in range(255):
    x = i % row
    y = i / row
    app.stroke(' ', i, i)
    app.point(start_x + x, start_y + y)

app.run()
