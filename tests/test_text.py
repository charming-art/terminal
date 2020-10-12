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
    app.backgournd(' ')
    global x
    # app.log(text_width)
    # app.scale(2, 2)
    # app.text_size(1)
    app.translate(0, app.get_height() / 2)
    # app.rotate(app.PI)
    # app.text_leading(2)
    x += 0.5
    app.text_align(app.CENTER, app.MIDDLE)
    # app.rotate(app.PI / 4)
    app.text(face, x, 0)
    # app.no_loop()
    # pass


app.run()
