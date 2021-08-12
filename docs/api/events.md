# Events

Methods for listening and handling events.

## Keyboard

Methods for keyboard events.

<a name="get_key" href="#get_key">#</a> cm.**get_key**() : *string*

The system variable key always contains the value of the most recent key on the keyboard that was used (either pressed or released).

<a name="get_key_pressed" href="#get_key_pressed">#</a> cm.**get_key_code**() : *boolean*

The boolean system variable key_pressed is true if any key is pressed and false if no keys are pressed.

```py
import charming as cm


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()


@cm.draw
def draw():
    cm.background(' ')
    if cm.get_key_pressed():
        key = cm.get_key()
        if key == 'b' or key == 'B':
            cm.fill('O')
        else:
            cm.fill('+')
    cm.no_stroke()
    cm.rect(0, 0, 10, 10)


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_key.gif" width="100%"/>

<a name="get_key_code" href="#get_key_code">#</a> cm.**get_key_code**() : *number*

The variable keyCode is used to detect special keys such as the arrow keys (UP, DOWN, LEFT, and RIGHT) as well as ENTER, SPACE.

<a name="key_pressed" href="#key_pressed">#</a> cm.**key_pressed**(*foo*)

The function decorated by key_pressed decorator is called once every time a key is pressed.

```py
import charming as cm

# CODED, ESCAPE, LEFT, UP, RIGHT, DOWN, BACKSPACE, TAB, ENTER, SPACE

char = ''


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()


@cm.draw
def draw():
    cm.background(' ')
    cm.fill(char)
    cm.no_stroke()
    cm.rect(0, 0, 10, 10)


@cm.key_pressed
def key_pressed():
    global char
    if cm.get_key() == cm.CODED:
        if cm.get_key_code() == cm.UP:
            char = 'O'
        else:
            char = '+'


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_key_code.gif" width="100%"/>

<a name="key_released" href="#key_released">#</a> cm.**key_released**(*foo*)

The function decorated by key_released decorator is called once every time a key is released.

```py
import charming as cm

char = ''


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()


@cm.draw
def draw():
    cm.background(' ')
    cm.fill(char)
    cm.no_stroke()
    cm.rect(0, 0, 10, 10)


@cm.key_released
def key_released():
    global char
    if cm.get_key() == cm.CODED:
        if cm.get_key_code() == cm.UP:
            char = 'O'
        else:
            char = '+'


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_key_code.gif" width="100%"/>

<a name="key_typed" href="#key_typed">#</a> cm.**key_typed**(*foo*)

The function decorated by key_typed decorator is called once every time a key is typed.

```py
import charming as cm

char = ''


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()


@cm.draw
def draw():
    cm.background(' ')
    cm.fill(char)
    cm.no_stroke()
    cm.rect(0, 0, 10, 10)


@cm.key_typed
def key_typed():
    global char
    if cm.get_key() == cm.CODED:
        if cm.get_key_code() == cm.UP:
            char = 'O'
        else:
            char = '+'


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_key_code.gif" width="100%"/>

## Mouse

Methods for mouse events.

<a name="get_mouse_x" href="#get_mouse_x">#</a> cm.**get_mouseX**() : *number*

The system variable mouse_x always contains the current horizontal coordinate of the mouse.

<a name="get_mouse_y" href="#get_mouse_y">#</a> cm.**get_mouseY**() : *number*

The system variable mouse_y always contains the current vertical coordinate of the mouse.

```py
import charming as cm


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()


@cm.draw
def draw():
    cm.background(' ')
    mouse_x = cm.get_mouse_x()
    mouse_y = cm.get_mouse_y()
    cm.line(mouse_x, 0, mouse_x, cm.get_height())
    cm.line(0, mouse_y, cm.get_width(), mouse_y)


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_mouse_pos.gif" width="100%"/>

<a name="get_mouse_pressed" href="#get_mouse_pressed">#</a> cm.**get_mouse_pressed**() : *boolean*

The mouse_pressed variable stores whether or not a mouse button is currently being pressed.

<a name="get_mouse_button" href="#get_mouse_button">#</a> cm.**get_mouse_button**() : *boolean*

When a mouse button is pressed, the value of the system variable mouseButton is set to either LEFT, RIGHT, or CENTER, depending on which button is pressed.

```py
import charming as cm


@cm.setup
def setup():
    cm.full_screen()


@cm.draw
def draw():
    cm.no_stroke()
    if cm.get_mouse_pressed() and cm.get_mouse_button() == cm.LEFT:
        cm.fill('O')
    elif (cm.get_mouse_pressed() and cm.get_mouse_button() == cm.RIGHT):
        cm.fill('+')
    else:
        cm.fill('-')
    cm.rect(0, 0, 10, 10)


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_mouse_button.gif" width="100%"/>

<a name="mouse_clicked" href="#mouse_clicked">#</a> cm.**mouse_clicked**(*foo*)

```py
import charming as cm

char = 'O'


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()


@cm.draw
def draw():
    cm.background(' ')
    cm.fill(char)
    cm.rect(0, 0, 10, 10)


@cm.mouse_clicked
def mouse_clicked():
    global char
    if char == 'O':
        char = '+'
    else:
        char = 'O'


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_mouse_button.gif" width="100%"/>

<a name="mouse_pressed" href="#mouse_pressed">#</a> cm.**mouse_pressed**(*foo*)

The function decorated mouse_released decorator is called after a mouse button has been pressed.

```py
import charming as cm

char = 'O'


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()


@cm.draw
def draw():
    cm.background(' ')
    cm.fill(char)
    cm.rect(0, 0, 10, 10)


@cm.mouse_pressed
def mouse_pressed():
    global char
    if char == 'O':
        char = '+'
    else:
        char = 'O'


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_mouse_button.gif" width="100%"/>

<a name="mouse_released" href="#mouse_released">#</a> cm.**mouse_released**(*foo*)

```py
import charming as cm

char = 'O'


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()


@cm.draw
def draw():
    cm.background(' ')
    cm.fill(char)
    cm.rect(0, 0, 10, 10)


@cm.mouse_released
def mouse_released():
    global char
    if char == 'O':
        char = '+'
    else:
        char = 'O'


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_get_mouse_button.gif" width="100%"/>

## Cursor

Methods for cursor events.

<a name="get_cursor_x" href="#get_cursor_x">#</a> cm.**get_cursor_x**() : *number*

The system variable cursor_x always contains the current horizontal coordinate of the cursor.

<a name="get_cursor_y" href="#get_cursor_y">#</a> cm.**get_cursor_y**() : *number*

The system variable cursor_y always contains the current vertical coordinate of the cursor.

<a name="get_pcursor_x" href="#get_pcursor_x">#</a> cm.**get_pcursor_x**() : *number*

The system variable pcursor_x always contains the horizontal position of the cursor in the frame previous to the current frame.

<a name="get_pcursor_y" href="#get_pcursor_y">#</a> cm.**get_pcursor_y**() : *number*

The system variable pcursor_y always contains the vertical position of the cursor in the frame previous to the current frame.

<a name="cursor_moved" href="#cursor_moved">#</a> cm.**cursor_moved**(*foo*)

The function decorated cursor_moved decorator is called after a cursor moved.

<a name="cursor_pressed" href="#cursor_pressed">#</a> cm.**cursor_pressed**(*foo*)

The function decorated cursor_pressed decorator is called after a cursor pressed.

<a name="get_cursor_moved" href="#get_cursor_moved">#</a> cm.**get_cursor_moved**() : *number*

The boolean system variable cursor_moved is true if any cursor is pressed and false if cursor is not pressed.

```py
import charming as cm


@cm.setup
def setup():
    cm.full_screen()
    cm.set_cursor(cm.get_width() / 2, cm.get_height() / 2)


@cm.draw
def draw():
    cm.background(' ')
    # check if cursor is moving, otherwise draw hint message
    if not cm.get_cursor_moved():
        cm.translate(cm.get_width() / 2, cm.get_height() / 2)
        cm.text_align(cm.CENTER)
        cm.stroke(' ', cm.WHITE, cm.BLACK)
        cm.text('Pressed up/right/down/left arrow.', 0, 0)


# You can use cursor_pressed hooks instead of
# mouse_moved or mouse_dragged to do some effects.

@cm.cursor_pressed
def cursor_pressed():
    x = cm.get_cursor_x()
    y = cm.get_cursor_y()
    px = cm.get_pcursor_x()
    py = cm.get_pcursor_y()

    cm.stroke('@', cm.YELLOW, cm.RED)
    cm.fill('+', cm.GREEN, cm.BLUE)
    cm.ellipse(x, y, 10, 10)

    cm.stroke('+', cm.CYAN, cm.MAGENTA)
    cm.point(px, py)


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_event_cursor.gif" width="100%"/>