import sys
from .app import sketch
from .utils import logger


def log(*args, **kw):
    logger.debug(*args, **kw)
