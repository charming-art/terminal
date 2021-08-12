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
