# preview: https://raw.githubusercontent.com/charming-art/public-files/master/test_background.gif

import charming as cm


@cm.setup
def setup():
    c = cm.CColor('*')
    cm.full_screen()
    cm.frame_rate(2)
    cm.no_cursor()
    cm.background(c)  # use CColor


x = 0


@cm.draw
def draw():
    global x
    x += 1
    t = cm.get_frame_count() % 3

    if t == 0:
        cm.background('@')  # one channel
    elif t == 1:
        cm.background('+', cm.BLUE)  # two channel
    else:
        cm.background('-', cm.RED, cm.BLUE)  # three channel


    cm.fill('0', cm.YELLOW, cm.RED)
    cm.stroke('1', cm.GREEN, cm.BLUE)
    cm.rect(0, 0, 5, 5)


cm.run()
