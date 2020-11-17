import charming as app

app.full_screen()
# app.color_mode(app.RGB)
app.no_cursor()
app.color_mode(app.HSB)
cnt = 26
x = (app.get_width() - cnt) / 2
y = app.get_height() / 2
# start = app.CColor(bg=app.RED)
# end = app.CColor(bg=app.GREEN)
# start = app.CColor('a', bg=(255, 0, 0))
# end = app.CColor('z', bg=(0, 255, 0))
start = app.CColor(bg=(100, 100, 100))
end = app.CColor(bg=(200, 100, 100))
for i in range(cnt + 1):
    current = app.lerp_color(start, end, i / cnt)
    app.stroke(current)
    app.point(x + i, y)
app.run()
