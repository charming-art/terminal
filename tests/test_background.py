import charming as app


@app.setup
def setup():
    # app.size(30, 20)
    app.full_screen()
    # app.begin_log_frame_buffer()


x = 0
@app.draw
def draw():
    global x
    
    # if x % 2 == 0:
    #     app.background('*')
    # else:
    #     app.background('-')
    app.background(' ')
    # app.text_size(app.BIG)
    # app.text('hello world', 0, 0)
    app.fill('0', app.YELLOW, app.RED)
    app.stroke('1', app.GREEN, app.BLUE)
    app.rect(x, 0, 10, 10)
    x += 1
    # app.no_loop()
    # if x >= 10:
    #     app.no_loop()


app.run()
