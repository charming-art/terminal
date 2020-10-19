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
    # app.begin_log_frame_buffer()


x = 0


@app.draw
def draw():
    app.background(' ')
    # app.log(text_width)
    # app.scale(2, 2)
    # app.text_size(1)
    # app.translate(0, app.get_height() / 2)
    # app.rotate(app.PI)
    # app.text_leading(2)
    # app.text_align(app.CENTER, app.MIDDLE)
    # app.rotate(app.PI / 4)
    # app.scale(2)
    app.no_stroke()
    app.text('hello', 0, 0)
    # app.fill('*')
    # app.rect(0, 0, 1, 1)
    app.no_loop()
    # pass


app.run()
