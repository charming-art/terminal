# Structure

<a name="setup" href="#setup">#</a> cm.**setup**(*foo*)

The function decorated by setup() decorator is called once when the program starts. It's used to define initial environment properties such as screen size and background color and to load media such as images as the program starts.

```py
import charming as cm


a = 0


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()
    cm.background('O')
    cm.fill('+', cm.YELLOW, cm.CYAN)
    cm.no_stroke()


@cm.draw
def draw():
    global a
    cm.rect(a % cm.get_width(), 2, 2, cm.get_height() - 4)
    a += 1


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_setup.gif" />

<a name="draw" href="#draw">#</a> cm.**draw**(*foo*)

The function decorated by draw() called directly after setup(), it continuously executes the lines of code contained inside its block until the program is stopped or no_loop() is called. Note if no_loop() is called in setup(), draw() will still be executed once before stopping. draw() is called automatically and should never be called explicitly.

```py
import charming as cm

y = 0


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()
    cm.frame_rate(10)


@cm.draw
def draw():
    global y
    cm.background(' ')
    cm.line(0, y, cm.get_width(), y)
    y = (y + 1) % cm.get_height()


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_draw.gif" />

<a name="run" href="#run">#</a> cm.**run**()

Run the sketch or nothing magic will happen.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

cm.rect(0, 0, 5, 5)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_run.png" />

<a name="no_loop" href="#no_loop">#</a> cm.**no_loop**()

Stops Charming from continuously executing the code within draw(). If loop() is called, the code in draw() begins to run continuously again. If using no_loop() in setup(), it should be the last line inside the block.

<a name="loop" href="#loop">#</a> cm.**loop**()

By default, Charming loops through draw() continuously, executing the code within it. However, the draw() loop may be stopped by calling no_loop(). In that case, the draw() loop can be resumed with loop().

<a name="get_is_looping" href="#get_is_looping">#</a> cm.**get_is_looping**()

```py
import charming as cm

y = 0

@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()
    cm.frame_rate(10)


@cm.draw
def draw():
    global y
    cm.background(' ')
    cm.line(0, y, cm.get_width(), y)
    y = (y + 1) % cm.get_height()


@cm.mouse_clicked
def mouse_clicked():
    if cm.get_is_looping():
        cm.no_loop()
    else:
        cm.loop()


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_loop.gif" />

<a name="redraw" href="#redraw">#</a> cm.**redraw**()

Executes the code within draw() one time. This function allows the program to update the display window only when necessary, for example when an event registered by mouse_pressed() or key_pressed() occurs.

```py
import charming as cm

x = 0


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()
    cm.no_loop()


@cm.draw
def draw():
    global x
    cm.background(' ')
    cm.line(x, 0, x, cm.get_height())
    x = (x + 1) % cm.get_width()


@cm.mouse_clicked
def mouse_clicked():
    cm.redraw()


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_redraw.gif" />

<a name="push" href="#push">#</a> cm.**push**() <br/>
<a name="pop" href="#pop">#</a> cm.**pop**()

The push() function saves the current drawing style settings and transformations, while pop() restores these settings. Note that these functions are always used together. They allow you to change the style and transformation settings and later return to what you had. When a new state is started with push(), it builds on the current style and transform information.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

cm.ellipse(5, 5, 10, 5)

cm.push()
cm.fill('+', cm.YELLOW, cm.CYAN)
cm.stroke('O', cm.BLUE, cm.GREEN)
cm.translate(15, 0)
cm.ellipse(5, 5, 10, 5)
cm.pop()

cm.ellipse(35, 5, 10, 5)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_push.png" />

<a name="open_context" href="#open_context">#</a> cm.**open_context**()

The syntactic sugar for push() and pop().

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

cm.ellipse(5, 5, 10, 5)

with cm.open_context():
  cm.fill('+', cm.YELLOW, cm.CYAN)
  cm.stroke('O', cm.BLUE, cm.GREEN)
  cm.translate(15, 0)
  cm.ellipse(5, 5, 10, 5)

cm.ellipse(35, 5, 10, 5)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_push.png" />

<a name="exit" href="#exit">#</a> cm.**exit**()

Exit the sketch.

```py
import charming as cm


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()
    cm.color_mode(cm.RGB)


@cm.draw
def draw():
    b = cm.get_frame_count() % 255
    color = (0, 0, b)
    cm.background(' ', color, color)


@cm.mouse_clicked
def mouse_clicked():
    cm.exit()


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_exit.gif" />
