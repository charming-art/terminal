import types
import sys
from .api import *
from . import api
from .common import capture_exception

charming = sys.modules[__name__]


def attributes_mapping(source, target):
    '''
    Capture exception when call all of charming function in order to call context.close().
    This will ensure that exit the program without staying funny terminal state, 
    espicailly in static mode.
    '''
    for name in dir(source):
        if not name.startswith('__'):
            attr = getattr(source, name)
            if hasattr(attr, '__call__'):
                attr = capture_exception(attr)
                setattr(target, name, attr)


attributes_mapping(api, charming)
