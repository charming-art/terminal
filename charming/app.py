from sys import platform
from .core import Sketch
from .core import Renderer
from .core import BROWSER
from .core import WINDOWS


def get_components_by_platform(platform):
    if platform == WINDOWS:
        from .core import WindowsContext
        from .core import PILImageLoader
        from .core import LocalTimer
        return (WindowsContext(), PILImageLoader(), LocalTimer())
    elif platform == BROWSER:
        from .core import BrowserContext
        from .core import BrowserImageLoader
        from .core import BrowserTimer
        return (BrowserContext(), BrowserImageLoader(), BrowserTimer())
    else:
        from .core import CursesContext
        from .core import PILImageLoader
        from .core import LocalTimer
        return (CursesContext(), PILImageLoader(), LocalTimer())


context, image_loader, timer = get_components_by_platform(platform)
renderer = Renderer()
sketch = Sketch(renderer, context, image_loader, timer)
