import charming as app

globe_frames = None
fall_frames = None


@app.setup
def setup():
    global globe_frames, fall_frames
    app.full_screen(app.DOUBLE)
    app.frame_rate(5)
    app.no_cursor()
    fall_frames = app.load_image("images/fall.gif")
    globe_frames = app.load_image("images/globe.gif")


@app.draw
def draw():
    app.background()
    width = app.get_width()
    height = app.get_height()
    w = 30
    h = 30
    x = (width - w) / 2
    y = (height - h) / 2
    fall_img = fall_frames[app.get_frame_count() % len(fall_frames)]
    globe_img = globe_frames[app.get_frame_count() % len(globe_frames)]

    app.image(globe_img, x, y, w, h)
    app.image(fall_img, 0, 0, width, height)


if __name__ == "__main__":
    app.run()
