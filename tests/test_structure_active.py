import charming as app


@app.setup
def setup():
    ''' Only run once, define initial enviroment properties'''
    app.size(40, 20)
    app.no_cursor()


x = 0
loop = True


@app.draw
def draw():
    ''' The main loop for the program '''
    global x
    x += 0.5

    app.background(' ')
    app.stroke('@', app.RED)
    app.rect(x, 2, 5, 5)

    # Save the styles and transforms
    app.push()
    app.stroke('#', app.YELLOW)
    app.translate(10, 0)
    app.rect(x, 2, 5, 5)
    app.pop()

    # Anohter way for saving the styles and transforms
    with app.open_context():
        app.stroke('!', app.BLUE)
        app.translate(0, 10)
        app.rect(x, 2, 5, 5)

    app.rect(x + 10, 12, 5, 5)

    if x > app.get_width():
        x = 0


@app.mouse_pressed
def mouse_pressed():
    ''' Toggle the animation by clicking the screen '''
    global loop
    if loop:
        app.no_loop()
    else:
        app.loop()

    loop = not loop


@app.key_typed
def key_typed():
    ''' Executes the code within draw() one time '''
    global loop

    if app.get_key() == "q":
        app.exit()
    else:
        if loop:
            app.no_loop()
            loop = False
        app.redraw()


app.run()
