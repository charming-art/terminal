from charming import Charming

app = Charming()

x = 0
y = 0


@app.setup
def setup():
    app.size(30, 30)


@app.draw
def draw():
    app.background(' ', app.WHITE)
    app.stroke('@', app.BLUE)
    app.fill('', app.YELLOW)
    app.rect(x, y, 10, 5)


@app.keyPressed
def keyPressed():
    global x, y
    if app.key == app.RIGHT:
        x += 1
    elif app.key == app.LEFT:
        x -= 1
    elif app.key == app.UP:
        y -= 1
    elif app.key == app.DOWN:
        y += 1


@app.mouseClicked
def mouseClicked():
    global x, y
    x = app.mouseX
    y = app.mouseY


app.run()
