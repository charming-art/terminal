---
id: events
title: Event
---
Events means you can bring life to your artworks, because you can interact with it and it will give you feedback.

Similar to `setup` and `draw` function, you must register event listeners (`mouse_pressed`, `key_pressed`, etc.) by decorators.

## Cursor event

Besides mouse events and keyboard events, Charming provide a unique type of events which deeply embed in terminal: **cursor events**, which will be triggered if you type or press the `UP/Right/DOWN/LEFT` arrow keys to move the cursor on the terminal.

```py
''' charming: event'''

import charming as app

@app.setup
def setup():
    app.full_screen()
    app.color_mode(app.RGB)
    width = app.get_width()
    height = app.get_height()

    # set the cursor at the middle of the screen
    # and hide it
    app.set_cursor(width / 2, height / 2)
    app.no_cursor()

points = []

@app.draw
def draw():
    app.background(' ')
    for i, p in enumerate(points):
        c = app.map(i, 0, len(points), 0, 255)
        app.stroke('@', (c, 0, 0), (c, c, 0))
        app.point(p.x, p.y)

@app.cursor_pressed
def cursor_pressed():
    # add a point if cursor moved
    x = app.get_cursor_x()
    y = app.get_cursor_y()
    points.append(app.CVector(x, y))

app.run()
```

![image](https://raw.githubusercontent.com/charming-art/public-files/master/cursor_event.gif)

<!-- ## Mouse Event

## Keyboard Event

## Window Event -->
