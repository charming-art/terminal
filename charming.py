import os
import time
import curses


class Charming:

    def __init__(self):
        self.win = curses.initscr()
        self.win.keypad(1)  # Enable arrow keys
        self.win.nodelay(1)  # Do not wait for keypress

        self.setup_callback = None
        self.draw_callback = None
        self.keyPressed_callback = None
        self.sleep_time = 0.1

        self.width = 100
        self.height = 100
        self.buffer = []

        self.key = -1
        self.mouseX = -1
        self.mouseY = -1

        # colors type
        self.WHITE = 1
        self.RED = 2
        self.YELLOW = 3
        self.BLUE = 4

        # chars
        self.fill_ch = ' '
        self.stroke_ch = '*'
        self.corner_ch = '*'

        # colors
        self.fill_color = 0
        self.stroke_color = 0
        self.corner_color = 0

        self.RIGHT = 261
        self.LEFT = 260
        self.UP = 259
        self.DOWN = 258

    def size(self, w, h):
        self.width = w
        self.height = h
        self.buffer = [[(self.fill_ch, self.fill_color) for _ in range(
            self.width)] for _ in range(self.height)]

    def rect(self, x, y, width, height):
        for i in range(x, x + width):
            for j in range(y, y + height):
                # corner
                if (i == x or i == x + width - 1) and (j == y or j == y + height - 1):
                    self.buffer[j][i] = (self.corner_ch, self.corner_color)
                elif (i == x or i == x + width - 1) or (j == y or j == y + height - 1):
                    self.buffer[j][i] = (self.stroke_ch, self.stroke_color)
                else:
                    self.buffer[j][i] = (self.fill_ch, self.fill_color)

    def background(self, ch, color):
        self.buffer = [[(ch, color) for j in range(self.width)]
                       for i in range(self.height)]

    def fill(self, ch, color):
        self.fill_ch = ch
        self.fill_color = color

    def stroke(self, ch, color):
        self.stroke_ch = ch
        self.stroke_color = color

    def corner(self, ch, color):
        self.corner_ch = ch
        self.corner_color = color

    def setup(self, foo):
        curses.start_color()  # Enables colors
        curses.init_pair(self.WHITE, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(self.RED, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(self.YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(self.BLUE, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.curs_set(0)  # Hide cursor
        curses.cbreak()  # Read keys instantaneously
        curses.noecho()  # Do not print stuff when keys are pressed
        curses.mousemask(1)
        self.setup_callback = foo

    def keyPressed(self, foo):
        self.keyPressed_callback = foo

    def mouseClicked(self, foo):
        self.mouseClicked_callback = foo

    def draw(self, foo):
        self.draw_callback = foo

    def run(self):
        self.setup_callback()
        while True:

            # keydown event
            self.key = self.win.getch()
            if self.key != -1:
                self.keyPressed_callback()

            # mouse event
            if self.key == curses.KEY_MOUSE:
                _, mx, my, _, _ = curses.getmouse()
                self.mouseX = mx
                self.mouseY = my
                self.mouseClicked_callback()

            # draw
            self.draw_callback()
            for i in range(self.height):
                for j in range(self.width):
                    ch, color = self.buffer[i][j]
                    self.win.addstr(
                        i, j, ch, curses.color_pair(color))

            time.sleep(self.sleep_time)


charming = Charming()
