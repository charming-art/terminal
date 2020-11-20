import charming as app

face = """
    ______
  .`      `.
 /   -  -   \\
|     __     |
|            |
 \\          /
  '.______.'
"""


@app.setup
def setup():
    app.full_screen()


x = 0


@app.draw
def draw():
    app.background(' ')
    # app.scale(2)
    # app.stroke(" ", app.RED, app.YELLOW)
    # app.text_size(3)
    # app.text_leading(2)
    # app.translate(0, app.get_height() / 2)
    # app.rotate(app.PI)
    # app.text_leading(2)
    # app.text_align(app.CENTER, app.MIDDLE)
    # app.rotate(app.PI / 4)
    # app.scale(2)
    # app.no_stroke()
    # text = "hello\nworld"
    # app.text_leading(2)
    # w = app.text_width(text)
    # h = app.text_height(text)

    # app.stroke(" ", fg=app.YELLOW, bg=app.GREEN)
    app.translate(app.get_width() / 2, app.get_height() / 2)
    app.text_align(app.CENTER, app.MIDDLE)
    app.text_size(app.BIG)
    # app.text(face, 2, 2)
    # app.text('hello world', 0, 0)
    app.text('charming', 0, 0)
    # app.text("|     __     |", 10, 2)
    # app.scale(2)
    # app.text('hello world', 2, 2)
    # app.fill('*')
    # app.rect(0, 0, 1, 1)
    app.no_loop()


app.run()
