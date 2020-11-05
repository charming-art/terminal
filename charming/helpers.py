import sys
from .app import sketch
from .utils import logger

def log(msg):
    logger.log(msg)


def begin_log_frame_buffer():
    sketch.is_log_frame_buffer = True


def end_log_frame_buffer():
    sketch.is_log_frame_buffer = False
