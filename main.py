from charming import charming as cm

x = 0
y = 0
colors = [cm.WHITE, cm.YELLOW, cm.BLUE, cm.RED]
activeIndex = 0


@cm.setup
def setup():
    cm.size(30, 30)


@cm.draw
def draw():
    cm.background(' ', cm.WHITE)
    cm.corner('@', cm.RED)
    cm.stroke('@', cm.BLUE)
    cm.fill('', cm.YELLOW)
    cm.rect(x, y, 10, 5)


@cm.keyPressed
def keyPressed():
    global x, y
    if cm.key == cm.RIGHT:
        x += 1
    elif cm.key == cm.LEFT:
        x -= 1
    elif cm.key == cm.UP:
        y -= 1
    elif cm.key == cm.DOWN:
        y += 1


@cm.mouseClicked
def mouseClicked():
    global x, y, activeIndex
    x = cm.mouseX
    y = cm.mouseY
    activeIndex = (activeIndex + 1) % len(colors)


cm.run()
