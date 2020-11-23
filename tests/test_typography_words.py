import charming as app

app.full_screen()
app.no_cursor()
app.stroke(fg=app.YELLOW, bg=app.RED)
text = "hello"

# normal text
ntw = app.text_width(text)
app.text(text, 5, 5)

with app.open_context():
    app.translate(15, 5)
    app.scale(2)
    app.text(text, 0, 0)

# big text
app.text_size(app.BIG)
btw = app.text_width(text)
app.text(text, ntw + 25, 5)

# large text
app.text_size(app.LARGE)
app.text(text, ntw + btw + 35, 5)

with app.open_context():
    app.text_size(app.BIG)
    app.stroke('+', app.GREEN, app.BLUE)
    app.translate(app.get_width() / 2, app.get_height() / 2)
    app.text_align(app.CENTER, app.MIDDLE)
    th = app.text_height('charming')
    app.text('charming', 0, 0)

    font = app.get_font_list()[3]
    app.stroke(fg=app.CYAN, bg=app.MAGENTA)
    app.text_font(font)
    app.text('awesome', 0, th + 2)

app.run()
