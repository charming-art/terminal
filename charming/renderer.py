import time


class Renderer(object):

    setup_hook = None
    draw_hook = None
    frame_rate = 30

    def __init__(self):
        pass

    def config(self, hooks_map):
        self.setup_hook = hooks_map['setup']
        self.draw_hook = hooks_map['draw']

    def run(self):
        self.setup_hook()
        while True:
            self.draw_hook()
            time.sleep(1 / self.frame_rate)
