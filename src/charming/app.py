from sys import platform
from .core import Sketch
from .core import Renderer
from .core import WINDOWS


def get_context_by_platform(platform):
    if platform == WINDOWS:
        from .core import WindowsContext
        return WindowsContext()
    else:
        from .core import CursesContext
        return CursesContext()

context = get_context_by_platform(platform)
renderer = Renderer()
sketch = Sketch(renderer, context)
