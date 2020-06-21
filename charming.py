import os
import time

class Charming:

    def __init__(self):
        self.setup_callback = None
        self.draw_callback = None
        self.sleep_time = 0.1

        self.width = 100
        self.height = 100
        self.buffer = []

        self.fill_ch = '*'
        self.stroke_ch = '*'
        self.corner_ch = '*'

        self.fill_color = 'white'
        self.stroke_color = 'white'
        self.corner_color = 'white'

    def size(self, w, h):
        self.width = w
        self.height = h
        self.buffer = [[self.fill_ch for _ in range(
            self.width)] for _ in range(self.height)]

    def rect(self, x, y, width, height):
        pass
        # for i in range(x, x + width):
        #     for j in range(x, y + height):
        #         if (i == x or i == x + width) and (j == y or j == y + height):
        #             self.buffer[i][j] = corner_ch
        #         elif:
        #             pass
        #         else:
        #             self.buffer[i][j] = fill_ch

    def background(self, ch):
        self.buffer = [[ch for j in range(self.width)]
                       for i in range(self.height)]

    def fill(self, ch):
        self.fill_ch = ch

    def stroke(self, ch):
        self.stroke_ch = ch

    def corner(self, ch):
        self.corner_ch = ch

    def setup(self, foo):
        self.setup_callback = foo

    def draw(self, foo):
        self.draw_callback = foo

    def run(self):
        self.setup_callback()
        while True:
            self.draw_callback()
            for i in range(self.height):
                for j in range(self.width):
                    print(self.buffer[i][j], end='')
                print()
            time.sleep(self.sleep_time)

charming = Charming()
