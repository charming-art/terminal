import sys
from .app import sketch
from .core import logger


def log(*args, **kw):
    logger.debug(*args, **kw)


def begin_log_frame_buffer():
    sketch.is_log_frame_buffer = True


def end_log_frame_buffer():
    sketch.is_log_frame_buffer = False
