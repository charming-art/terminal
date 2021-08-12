import charming as cm

chars = ['💘', '🌈', 'A', ('⏰', 2), '🧚', '爱']
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

    # polygan
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
