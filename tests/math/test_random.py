import charming as cm


bar_width = 5
bar_count = 0
bars = []


@cm.setup
def setup():
    global bars, bar_count
    cm.full_screen()
    cm.no_cursor()
    bar_count = cm.floor(cm.get_width() / bar_width)
    bars = [0 for _ in range(bar_count)]


@cm.draw
def draw():
    global bars
    i = int(cm.random(bar_count))
    bars[i] += 1

    cm.background(' ')
    cm.fill('Q')
    cm.no_stroke()

    for index, bar_height in enumerate(bars):
        cm.rect(
            bar_width * index,
            cm.get_height() - bar_height,
            bar_width,
            bar_height
        )


cm.run()
