import charming as app

app.size(30, 30)
app.stroke('@')
app.translate(app.get_width() / 2, app.get_height() / 2)
# app.rotate(app.PI / 3)
app.fill('+')
app.rect(0, 0, 10, 10)
app.run()