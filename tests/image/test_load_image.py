import charming as cm

frames = None


@cm.setup
def setup():
    global frames
    cm.full_screen()
    cm.no_cursor()
    frames = cm.load_image('../assets/images/test.gif')


@cm.draw
def draw():
    cm.background(' ')
    index = int(cm.get_frame_count() / 2) % len(frames)
    frame = frames[index]
    cm.image(frame, 0, 0, 30, 15)


cm.run()
