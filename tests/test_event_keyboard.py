import charming as app

msg = "" # the message to show
cnt = 0 # the left time for the message being big


@app.setup
def setup():
    app.full_screen()
    app.no_cursor()


@app.draw
def draw():
    global cnt, msg
    app.background(' ')
    app.translate(app.get_width() / 2, app.get_height() / 2)
    app.text_align(app.CENTER, app.MIDDLE)

    # Choose the right text size to display by cnt
    if cnt > 0:
        app.text_size(app.BIG)
        cnt -= 1
        if cnt == 0:
            msg = ""
    else:
        app.text_size(app.NORMAL)

    # Choose the right text to display by key pressed status
    if app.get_key_pressed():
        app.text(msg, 0, 0)
    else:
        hint = 'Input and press Enter.' if len(msg) == 0 else f'Keys:{msg}'
        app.text(hint, 0, 0)


@app.key_typed
def key_typed():
    # Type ascii to input
    # Type backspace to delete
    # Type enter to highlight

    global msg, cnt
    key = app.get_key()
    if key == app.CODED:
        key_code = app.get_key_code()
        if key_code == app.BACKSPACE:
            msg = msg[:-1] if len(msg) > 0 else ""
        elif key_code == app.ENTER:
            cnt = 20
    else:
        msg += key

@app.key_pressed
def key_pressed():
    app.translate(app.get_width() / 2, app.get_height() / 2 + 5)
    app.fill(bg=app.BLUE)
    app.ellipse(0, 0, 5, 5)

@app.key_released
def key_released():
    app.translate(app.get_width() / 2, app.get_height() / 2 + 5)
    app.fill(bg=app.RED)
    app.ellipse(0, 0, 5, 5)


app.run()
