# Environment

Methods for set and get runtime environment.

<a name="cursor" href="#cursor">#</a> cm.**cursor**()

Set the cursor visible.

<a name="set_cursor" href="#set_cursor">#</a> cm.**set_cursor**(*x*, *y*)

Set the positions of cursor in cells.

```py
import charming as cm

cm.full_screen()
cm.cursor()
cm.set_cursor(cm.get_width() / 2, cm.get_height() / 2)
cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_cursor.png" />

<a name="no_cursor" href="#no_cursor">#</a> cm.**no_cursor**()

Hide the cursor.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_no_cursor.png" />

<a name="frame_rate" href="#frame_rate">#</a> cm.**frame_rate**(*rate*)

Specifies the number of frames to be displayed every second. For example, the function call frameRate(30) will attempt to refresh 30 times a second. If the processor is not fast enough to maintain the specified rate, the frame rate will not be achieved. Setting the frame rate within setup() is recommended.

<a name="get_frame_count" href="#get_frame_count">#</a> cm.**get_frame_count**() : *number*

The system variable frameCount contains the number of frames that have been displayed since the program started.

```py
import charming as cm


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()
    cm.frame_rate(1)


@cm.draw
def draw():
    cm.background(' ')
    cm.text_size(cm.BIG)
    cm.text_align(cm.CENTER, cm.MIDDLE)
    cm.text(cm.get_frame_count(), cm.get_width() / 2, cm.get_height() / 2)


cm.run()

```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_frame_rate.gif" />

<a name="full_screen" href="#full_screen">#</a> cm.**full_screen**(*mode=SINGLE | DOUBLE*)

Sets the sketch to fill the entire terminal.

The default mode is single mode which means render each character with only one cell. It works fine with character which take only one cell such as 'A', ';', etc.

```py
import charming as cm

x = 0


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()


@cm.draw
def draw():
    global x
    cm.background(' ')
    cm.rect(x, 0, 10, 10)
    x += 1


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_full_screen_single.gif" />

The double render mode will use two cells to render a shape character. If a character is two-cell width (💘, 🌈, etc.), it only render once while one-cell width character (a, ;, etc.) will be render twice.

In some case, Charming cant not get the right width for characters, you can use a tuple (ch, width) to specify the width of character to avoid unexpected mess.

In double mode, a text character will still use one cell to render for one-cell width.

```py
import charming as cm



chars = ['💘', '🌈', ('⏰', 2), '🧚', '爱', 'a']
texts = [
    'hello world',
    '🚀🚀h',
    'h🚀llo'
]

x = 0


@cm.setup
def setup():
    cm.full_screen(cm.DOUBLE)
    cm.frame_rate(2)
    cm.no_cursor()


@cm.draw
def draw():
    global x
    size = 5
    ch = chars[cm.get_frame_count() % len(chars)]
    y = 10
    x += 2

    cm.background(" ")
    cm.no_stroke()
    cm.fill(ch)

    # polygon
    cm.begin_shape()
    cm.vertex(x, y)
    cm.vertex(x + size, y)
    cm.vertex(x + size, y - size)
    cm.vertex(x + size * 2, y)
    cm.vertex(x, y + size * 2)
    cm.end_shape(cm.CLOSE)

    # text
    cm.stroke()
    for i, t in enumerate(texts):
        cm.text(t, 0, i)


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_full_screen_double.gif" />

<a name="get_height" href="#get_height">#</a> cm.**get_height**() : *number*

System variable that stores the height of the drawing canvas.

<a name="get_width" href="#get_width">#</a> cm.**get_width**() : *number*

System variable that stores the width of the drawing canvas.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.point(cm.get_width() / 2, cm.get_height() / 2)
cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_dimensions.png" />

<a name="size" href="#size">#</a> cm.**get_width**(*width*, *height*, *mode=SINGLE | DOUBLE*)

Sets the dimensions of it in cells for the sketch.

The default mode is single mode which means render each character with only one cell. It works fine with character which take only one cell such as 'A', ';', etc.

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_size_single.gif" />

The double render mode will use two cells to render a shape character. If a character is two-cell width (💘, 🌈, etc.), it only render once while one-cell width character (a, ;, etc.) will be render twice.

In some case, Charming cant not get the right width for characters, you can use a tuple (ch, width) to specify the width of character to avoid unexpected mess.

In double mode, a text character will still use one cell to render for one-cell width.

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_size_double.gif" />
