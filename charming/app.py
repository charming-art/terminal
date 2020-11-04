from sys import platform
from .core import Sketch, Renderer


def get_components_by_platform(platform):
    if platform == "win32":
        from .core import WindowsContext
        from .core import PILImageLoader
        return (WindowsContext(), PILImageLoader())
    elif platform == "brython":
        from .core import BrowserContext
        from .core import BrowserImageLoader
        return (BrowserContext(), BrowserImageLoader())
    else:
        from .core import CursesContext
        from .core import PILImageLoader
        return (CursesContext(), PILImageLoader())


context, image_loader = get_components_by_platform(platform)
renderer = Renderer()
sketch = Sketch(renderer, context, image_loader)
