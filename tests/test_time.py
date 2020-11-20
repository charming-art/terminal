import charming as app


@app.setup
def setup():
    app.full_screen()
    app.no_cursor()


@app.draw
def draw():
    app.background(' ')
    date = f'{app.year()} . {app.month()} . {wrap(app.day())}'
    time = f'{wrap(app.hour())} : {wrap(app.minute())} : {wrap(app.second())}'

    app.text_align(app.CENTER)
    app.text_size(app.BIG)
    h1 = app.text_height(date)
    h = h1 + 10

    app.translate(app.get_width() / 2, (app.get_height() - h) / 2)
    app.text(date, 0, 0)
    app.text(time, 0, 10)


def wrap(n):
    return f'0{n}' if n < 10 else n


app.run()
