from sys import platform
from .core import Sketch, Renderer


def get_context_by_platform(platform):
    if platform == "win32":
        from .core import WindowsContext
        return WindowsContext()
    elif platform == "brython":
        from .core import BrowserContext
        return BrowserContext()
    else:
        from .core import CursesContext
        return CursesContext()


context = get_context_by_platform(platform)
renderer = Renderer()
sketch = Sketch(renderer, context)
