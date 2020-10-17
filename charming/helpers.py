import logging
from .app import sketch

logging.basicConfig(filename='charming.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def log(msg):
    logger.debug(msg)


def begin_log_frame_buffer():
    sketch.is_log_frame_buffer = True


def end_log_frame_buffer():
    sketch.is_log_frame_buffer = False
