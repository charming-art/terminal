import sys
from .app import sketch
from .utils import logger


def debug(msg, *args, **kw):
    logger.debug(msg, *args, **kw)
