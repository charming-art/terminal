from .app import sketch
from .utils import logger


def print(*args, **kw):
    msg = ""
    for arg in args:
        msg += f'{arg.__str__()}, '

    if len(kw) != 0:
        msg += kw.__str__()
    logger.debug(msg)


def check_params():
    sketch._check_params = True