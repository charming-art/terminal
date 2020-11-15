import charming as app

app.full_screen()
app.color_mode(app.RGB)
# app.color_mode(app.HSB)
cnt = 5
x = (app.get_width() - cnt) / 2
y = app.get_height() / 2
# start = app.RED
# end = app.GREEN
start = (255, 0, 0)
end = (0, 255, 0)
# start = (100, 100, 100)
# end = (200, 100, 100)
for i in range(cnt):
    current = app.lerp_color(start, end, i / cnt)
    app.stroke(bg=current)
    app.point(x + i, y)
app.run()
