'''
Use snake to write a poetry: 
    title: This Is Just To Say
    link: https://www.poetryfoundation.org/poems/56159/this-is-just-to-say
'''
import charming as app

# directions
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

# global vars
poetry = "I have eaten the plums that were in the icebox and which you were probably saving for breakfast Forgive me they were delicious so sweet and so cold"
snake = []
index = 0
direction = int(app.random(4))
food = None
interval = 4
game_over = False


@app.setup
def setup():
    app.full_screen()
    app.no_cursor()
    app.color_mode(app.HSB)
    init_game()


@app.draw
def draw():
    app.background(' ')
    if app.get_frame_count() % interval == 0:
        update_snake()
    collision_detection()
    draw_snake()
    draw_food()


@app.cursor_moved
def cursor_moved():
    global direction
    key_code = app.get_key_code()
    if key_code == app.LEFT:
        direction = LEFT
    elif key_code == app.RIGHT:
        direction = RIGHT
    elif key_code == app.DOWN:
        direction = DOWN
    elif key_code == app.UP:
        direction = UP


@app.key_typed
def key_typed():
    if game_over:
        init_game()


def init_game():
    global snake, index, direction, game_over
    game_over = False
    x0 = app.get_width() / 2
    y0 = app.get_height() / 2
    app.set_cursor(x0, y0)
    index = 0
    direction = int(app.random(4))
    snake = [[x0, y0, 0]]
    generate_food()
    app.loop()


def draw_snake():
    for x, y, i in snake:
        h = app.map(i, 0, len(poetry), 0, 360)
        app.stroke(poetry[i], bg=(h, 100, 100))
        app.point(x, y)


def draw_food():
    h = app.map(food[2], 0, len(poetry), 0, 360)
    app.stroke(poetry[food[2]], bg=(h, 100, 100))
    app.point(food[0], food[1])


def update_snake():
    global game_over
    for i in range(len(snake) - 1):
        p1 = snake[i]
        p2 = snake[i + 1]
        p1[0] = p2[0]
        p1[1] = p2[1]

    head = snake[-1]
    width = app.get_width()
    height = app.get_height()
    if direction == UP:
        next_y = (head[1] - 1) % height
        next_x = head[0]
    elif direction == DOWN:
        next_y = (head[1] + 1) % height
        next_x = head[0]
    elif direction == LEFT:
        next_x = (head[0] - 1) % width
        next_y = head[1]
    else:
        next_x = (head[0] + 1) % width
        next_y = head[1]

    if in_snake(next_x, next_y):
        app.no_loop()
        game_over = True
    else:
        head[0] = next_x
        head[1] = next_y


def in_snake(x, y):
    for p in snake:
        if p[0] == x and p[1] == y:
            return True
    return False


def collision_detection():
    global snake
    head = snake[-1]
    if head[0] == food[0] and head[1] == food[1]:
        snake.append([food[0], food[1], index])
        generate_food()


def generate_food():
    global food, index, game_over
    if index == len(poetry) - 1:
        game_over = True
        app.no_loop()
    else:
        index = index + 1
        x = int(app.random(app.get_width()))
        y = int(app.random(app.get_height()))
        while in_snake(x, y):
            x = int(app.random(app.get_width()))
            y = int(app.random(app.get_height()))
        food = [x, y, index]


app.run()
