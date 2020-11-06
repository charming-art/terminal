from sys import platform
from .core import Sketch, Renderer


def get_components_by_platform(platform):
    if platform == "win32":
        from .core import WindowsContext
        from .core import PILImageLoader
        from .core import LocalTimer
        return (WindowsContext(), PILImageLoader(), LocalTimer())
    elif platform == "brython":
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
