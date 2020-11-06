import charming as app

x = 0


@app.setup
def setup():
    # app.full_terminal()
    # app.terminal_size(800, 600)
    # app.full_screen()
    app.size(25, 20)
    app.no_cursor()


@app.draw
def draw():
    # app.log('hello world')
    # app.background(' ')
    # global x
    # x += 1
    app.stroke('🌈')
    app.rect(x, 0, 1, 1)
    app.no_loop()


app.run()
