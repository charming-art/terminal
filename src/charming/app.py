from sys import platform
from .core import Sketch
from .core import Renderer
from .core import BROWSER
from .core import WINDOWS


def get_components_by_platform(platform):
    if platform == WINDOWS:
        from .core import WindowsContext
        from .core import LocalTimer
        return WindowsContext(),  LocalTimer() # pylint: disable=abstract-class-instantiated
    elif platform == BROWSER:
        from .core import BrowserContext
        from .core import BrowserTimer
        return BrowserContext(), BrowserTimer() # pylint: disable=abstract-class-instantiated
    else:
        from .core import CursesContext
        from .core import LocalTimer
        return CursesContext(),  LocalTimer()


context, timer = get_components_by_platform(platform)
renderer = Renderer()
sketch = Sketch(renderer, context, timer)
