import charming as cm
from random import choice


poetry = "I have eaten the plums that were in the icebox and which you were probably saving for breakfast Forgive me they were delicious so sweet and so cold"
directions = [cm.LEFT, cm.RIGHT, cm.UP, cm.DOWN]
snake = []
index = 0
direction = directions[0]
food = None
game_over = False


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()
    cm.color_mode(cm.HSB)
    init_game()


@cm.draw
def draw():
    cm.background(' ')
    if cm.get_frame_count() % 4 == 0:
        update_snake()
    collision_detection()
    draw_snake()
    draw_food()


@cm.cursor_moved
def cursor_moved():
    global direction
    direction = cm.get_key_code()


@cm.key_typed
def key_typed():
    if game_over:
        init_game()


def init_game():
    global snake, index, direction, game_over
    game_over = False
    index = 0
    direction = choice(directions)
    x0, y0 = int(cm.get_width() / 2), int(cm.get_height() / 2)
    snake = [[x0, y0, 0]]
    generate_food()

    cm.set_cursor(x0, y0)
    cm.loop()


def draw_snake():
    for x, y, i in snake:
        h = cm.map(i, 0, len(poetry), 0, 360)
        cm.stroke(poetry[i], bg=(h, 100, 100))
        cm.point(x, y)


def draw_food():
    h = cm.map(food[2], 0, len(poetry), 0, 360)
    cm.stroke(poetry[food[2]], bg=(h, 100, 100))
    cm.point(food[0], food[1])


def update_snake():
    global game_over
    for i in range(len(snake) - 1):
        p1, p2 = snake[i], snake[i + 1]
        p1[0], p1[1] = p2[0], p2[1]

    head = snake[-1]
    x_move = 0 if direction == cm.UP or direction == cm.DOWN else 1
    y_move = 0 if direction == cm.LEFT or direction == cm.RIGHT else 1
    x_d = 1 if direction == cm.RIGHT else -1
    y_d = 1 if direction == cm.DOWN else -1
    next_x = (head[0] + x_move * x_d) % cm.get_width()
    next_y = (head[1] + y_move * y_d) % cm.get_height()

    if in_snake(next_x, next_y):
        cm.no_loop()
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
        cm.no_loop()
    else:
        index = index + 1
        while True:
            x = int(cm.random(cm.get_width()))
            y = int(cm.random(cm.get_height()))
            if not in_snake(x, y):
                break
        food = [x, y, index]

if __name__ == "__main__":
    cm.run()
