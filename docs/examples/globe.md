# Cherry Blossom Globe

A cherry blossom gif and a globe gif can create a wonderful world by Charming. [[source](../../examples/globe.py)]

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/example_globe_globe.gif" height="200px"/> &emsp; <img src="https://raw.githubusercontent.com/charming-art/public-files/master/example_globe_fall.gif" height="200px" />

![preview.md](https://raw.githubusercontent.com/charming-art/public-files/master/example_globe.gif)

```py
import charming as cm

globe_frames = None
fall_frames = None


@cm.setup
def setup():
    global globe_frames, fall_frames
    cm.full_screen(cm.DOUBLE)
    cm.frame_rate(5)
    cm.no_cursor()
    fall_frames = cm.load_image("images/fall.gif")
    globe_frames = cm.load_image("images/globe.gif")


@cm.draw
def draw():
    cm.background()
    width = cm.get_width()
    height = cm.get_height()
    w = 30
    h = 30
    x = (width - w) / 2
    y = (height - h) / 2
    fall_img = fall_frames[cm.get_frame_count() % len(fall_frames)]
    globe_img = globe_frames[cm.get_frame_count() % len(globe_frames)]

    cm.image(globe_img, x, y, w, h)
    cm.image(fall_img, 0, 0, width, height)


if __name__ == "__main__":
    cm.run()

```
