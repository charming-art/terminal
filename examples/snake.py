import charming as app

poetry = "I have eaten the plums that were in the icebox and which you were probably saving for breakfast Forgive me they were delicious so sweet and so cold"
snake = []
index = 0
food = None

@app.setup
def setup():
    global snake
    app.full_screen()
    app.no_cursor()

    x0 = app.get_width() / 2
    y0 = app.get_height() / 2
    app.set_cursor(x0, y0)

    snake.append([x0, y0, 0])
    generate_food()

@app.draw
def draw():
    app.background(' ')

    # draw snakes
    for x, y, i in snake:
        app.stroke(poetry[i], bg=app.RED)
        app.point(x, y)

    # draw food
    app.stroke(poetry[food[2]], bg=app.RED)
    app.point(food[0], food[1])


@app.cursor_moved
def cursor_moved():
    app.print(snake)
    cursor_x = app.get_cursor_x()
    cursor_y = app.get_cursor_y()

    if cursor_x == food[0] and cursor_y == food[1]:
        snake.append([cursor_x, cursor_y, index])
        generate_food()
    else:
        for i in range(len(snake) - 1):
            p1 = snake[i]
            p2 = snake[i + 1]
            p1[0] = p2[0]
            p1[1] = p2[1]
        snake[-1][0] = cursor_x
        snake[-1][1] = cursor_y


def generate_food():
    global food, index
    index = (index + 1) % len(poetry)
    x = app.random(app.get_width())
    y = app.random(app.get_height())
    food = [int(x), int(y), index]


app.run()