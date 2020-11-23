import sys
from .app import sketch
from .utils import logger


def print(*args, **kw):
    msg = ""
    for arg in args:
        msg += f'{arg.__str__()}, '

    if len(kw) != 0:
        msg += kw.__str__()
    logger.debug(msg)


def no_check():
    sketch._check_params = False
