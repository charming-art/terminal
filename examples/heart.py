import charming as cm


@cm.setup
def setup():
    cm.full_screen(cm.DOUBLE)
    cm.rect_mode(cm.RADIUS)
    cm.ellipse_mode(cm.RADIUS)
    cm.no_cursor()
    cm.frame_rate(10)


@cm.draw
def draw():
    size = 8
    x = cm.get_frame_count() / 2
    n1 = easing(x, size)
    n2 = easing(x + cm.PI, size)

    cm.background(" ")
    cm.no_stroke()
    cm.translate(cm.get_width() / 2, cm.get_height() / 2)
    cm.rotate(cm.QUARTER_PI)

    cm.fill('💘')
    cm.square(0, 0, size)
    cm.circle(0, -n1, size)
    cm.circle(n2, 0, size)


def easing(x, scale=1):
    p = cm.TAU * 2
    x = x - (x // p) * p
    if x < cm.PI:
        return cm.cos(x) * scale
    elif x < cm.PI * 2:
        return - scale
    elif x < cm.PI * 3:
        return cm.cos(x + cm.PI) * scale
    else:
        return scale

if __name__ == "__main__":
    cm.run()
