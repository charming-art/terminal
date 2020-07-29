import os
import time
import curses


class Charming:

    def __init__(self):

        self.setup_callback = None
        self.draw_callback = None
        self.keyPressed_callback = None
        self.sleep_time = 0

        self.width = 30
        self.height = 30
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

        # colors
        self.fill_color = 0
        self.stroke_color = 0

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
        startX = max(0, x)
        endX = min(self.width, x + width)
        startY = max(0, y)
        endY = min(self.height, y + height)
        for i in range(startX, endX):
            for j in range(startY, endY):
                if (i == startX or i == endX - 1) or (j == startY or j == endY - 1):
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

    def setup(self, foo):
        self.stdscr = curses.initscr()
        self.screenHeight, self.screenWidth = self.stdscr.getmaxyx()

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

        x = int((self.screenWidth - self.width) / 2)
        y = int((self.screenHeight - self.height) / 2)
        self.win = curses.newwin(self.height + 2, self.width + 2, y, x)
        self.win.keypad(1)  # Enable arrow keys
        self.win.nodelay(1)  # Do not wait for keypress

        while True:
            # keydown event
            self.key = self.win.getch()
            if self.key != -1:
                self.keyPressed_callback()

            # mouse event
            if self.key == curses.KEY_MOUSE:
                _, mx, my, _, _ = curses.getmouse()
                self.mouseX = mx - x
                self.mouseY = my - y
                self.mouseClicked_callback()

            # draw
            self.draw_callback()
            for i in range(self.height):
                for j in range(self.width):
                    ch, color = self.buffer[i][j]
                    self.win.addstr(
                        i, j, ch, curses.color_pair(color))

            # time.sleep(self.sleep_time)
