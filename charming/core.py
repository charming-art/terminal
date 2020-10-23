import time
import logging
import sys
from abc import ABCMeta, abstractclassmethod
from . import constants
from .cmath import map
from .utils import Matrix
from .utils import get_char_width

logging.basicConfig(filename='charming.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Sketch(object):

    def __init__(self, renderer, context):
        self.renderer = renderer
        self.context = context

        self.frame_rate = 30
        self.is_loop = True
        self.frame_count = 0
        self.size = (10, 10)
        self.key = 0
        self.key_code = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.pmouse_x = 0
        self.pmouse_y = 0
        self.mouse_button = 0
        self.hooks_map = {
            'setup': lambda: None,
            'draw': lambda: None,
            'mouse_clicked': lambda: None,
            'mouse_pressed': lambda: None,
            'mouse_released': lambda: None,
            'mouse_moved': lambda: None,
            'mouse_dragged': lambda: None,
            'mouse_wheel': lambda: None,
            'key_typed': lambda: None,
            'key_pressed': lambda: None,
            'key_released': lambda: None,
            'window_resized': lambda: None,
        }

        self.is_log_frame_buffer = False

    def run(self):
        try:
            setup_hook = self.hooks_map['setup']
            draw_hook = self.hooks_map['draw']

            if not setup_hook or not draw_hook:
                return

            setup_hook()
            self.context.open(self.size)
            self.renderer.setup(self.size)

            while True:
                events = self.context.get_events()
                for e in events:
                    self._handle_event(e)

                if self.is_loop:
                    self.renderer.has_background_called = False
                    draw_hook()
                    self.renderer.render()

                    if self.renderer.has_background_called:
                        self.context.clear()

                    self.context.draw(self.renderer.frame_buffer,
                                      self.renderer.color_pair)

                    if self.is_log_frame_buffer == True:
                        self.renderer.log_frame_buffer()

                self.frame_count += 1
                time.sleep(1 / self.frame_rate)
        except Exception as e:
            logger.debug(e)
            raise e
        finally:
            self.context.close()

    def add_hook(self, name, hook):
        self.hooks_map[name] = hook

    def _handle_event(self, e):
        if e.type == 'mouse':
            self.pmouse_x = self.mouse_x
            self.pmouse_y = self.mouse_y
            self.mouse_x = e.x
            self.mouse_y = e.y
            mouse_hook = self.hooks_map['mouse_clicked']
            mouse_hook()
        elif e.type == "window":
            window_hook = self.hooks_map['window_resized']
            window_hook()
        elif e.type == "keyboard":
            self.key = e.key
            keyTyped_hook = self.hooks_map['key_typed']
            keyTyped_hook()


class Renderer(object):

    color_pair = []

    def __init__(self):
        self.frame_buffer = []
        self.shape_queue = []

        # styles
        self.fill_color = Color(' ')
        self.stroke_color = Color('*')
        self.stroke_weight = 0
        self.is_stroke_enabled = True
        self.is_fill_enabled = True
        self.rect_mode = constants.CORNER
        self.ellipse_mode = constants.CENTER
        self.text_align_x = constants.LEFT
        self.text_align_y = constants.TOP
        self.text_size = 1
        self.text_leading = self.text_size - 1
        self.text_space = 0

        self.has_background_called = False
        self.transform_matrix_stack = []
        self.size = (10, 10)

    def setup(self, size):
        self.size = size
        self._reset_frame_buffer()

    def render(self):
        while len(self.shape_queue) > 0:
            shape = self.shape_queue.pop(0)
            self._render_shape(shape)
        self.transform_matrix_stack.clear()
        self._adjust_unicode_char()

    def add_shape(self, shape):
        if shape.is_auto:
            shape.fill_color = self.fill_color
            shape.stroke_color = self.stroke_color
            shape.stroke_weight = self.stroke_weight
            shape.is_fill_enabled = self.is_fill_enabled
            shape.is_stroke_enabled = self.is_stroke_enabled
            shape.transform_matrix_stack = [
                m for m in self.transform_matrix_stack]
        self.shape_queue.append(shape)

    def set_frame_buffer(self, color):
        for i, _ in enumerate(self.frame_buffer):
            self.frame_buffer[i] = color

    def _reset_frame_buffer(self):
        width, height = self.size
        self.frame_buffer = [self.fill_color
                             for _ in range(width * height)]

    def _render_shape(self, shape):

        vertices = self._vertex_processing(
            shape.points,
            shape.stroke_color,
            shape.stroke_weight,
            shape.transform_matrix_stack)

        primitives = self._primitive_assembly(
            vertices,
            shape.primitive_type,
            shape.close_mode)

        fragments = self._rasterization(
            primitives,
            shape.fill_color,
            shape.is_stroke_enabled,
            shape.is_fill_enabled)

        fragments_clipped = self._clipping(fragments)

        self._fragment_processing(fragments_clipped)

    def _vertex_processing(self, points, stroke_color, stroke_weight, transform_matrix_stack):
        # transform
        tm = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        sm = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        while len(transform_matrix_stack) > 0:
            matrix = transform_matrix_stack.pop()
            tm = matrix * tm
            if matrix.type == "scale":
                sm = matrix * sm
        sx = sm[0][0]
        sy = sm[1][1]

        for p in points:
            mp = Matrix([[p.x], [p.y], [1]])
            tp = tm * mp
            p.x = tp[0][0]
            p.y = tp[1][0]
            p.weight_x = sx * stroke_weight if stroke_weight != 0 else sx - 1
            p.weight_y = sy * stroke_weight if stroke_weight != 0 else sy - 1

        # screen map && color
        for p in points:
            p.color = stroke_color
            p.x = int(p.x)
            p.y = int(p.y)

        return points

    def _primitive_assembly(self, vertices, primitive_type, close_mode):
        if primitive_type == constants.POLYGON:
            if close_mode == constants.CLOSE:
                vertices.append(vertices[0])
            ps = [vertices]
        elif primitive_type == constants.POINTS:
            ps = [[v] for v in vertices]
        elif primitive_type == constants.LINES:
            ps = [[vertices[i], vertices[i + 1]]
                  for i in range(len(vertices) - 1)
                  if i % 2 == 0]
        elif primitive_type == constants.TRIANGLES:
            ps = [[vertices[i], vertices[i + 1], vertices[i + 2], vertices[i]]
                  for i in range(len(vertices) - 2)
                  if i % 3 == 0]
        elif primitive_type == constants.TRIANGLE_STRIP:
            ps = [[vertices[i], vertices[i + 1], vertices[i + 2], vertices[i]]
                  for i in range(len(vertices) - 2)]
        elif primitive_type == constants.TRIANGLE_FAN:
            ps = [[vertices[0], vertices[i], vertices[i + 1], vertices[0]]
                  for i in range(1, len(vertices) - 1)]
        elif primitive_type == constants.QUADS:
            ps = [[vertices[i], vertices[i + 1], vertices[i + 2], vertices[i + 3], vertices[i]]
                  for i in range(len(vertices) - 3)
                  if i % 4 == 0]
        elif primitive_type == constants.QUAD_STRIP:
            ps = [[vertices[i], vertices[i + 1], vertices[i + 3], vertices[i + 2], vertices[i]]
                  for i in range(len(vertices) - 3)
                  if i % 2 == 0]
        elif primitive_type == constants.ARC:
            pass
        elif primitive_type == constants.CONTOUR:
            pass
        elif primitive_type == constants.CURVE:
            pass
        elif primitive_type == constants.BEZIER:
            pass

        return ps

    def _rasterization(self, primitives, fill_color, is_stroke_enabled, is_fill_enabled):
        fragments = []

        for vertices in primitives:
            fill_pixels = []
            # fill polygon
            if is_fill_enabled and len(vertices) > 2:
                fill_pixels += self._scan_line_filling(vertices, fill_color)

            # stroke polygon
            stroke_pixels = []
            if is_stroke_enabled:

                # draw origin points
                if len(vertices) == 1:
                    p = vertices[0]
                    stroke_pixels += self._rasterize_point(
                        p.x, p.y,
                        p.color,
                        p.weight_x, p.weight_y
                    )
                else:
                    for i, _ in enumerate(vertices):
                        if i < len(vertices) - 1:
                            stroke_pixels += self._rasterize_line(
                                vertices[i],
                                vertices[i + 1],
                            )

            pixels = fill_pixels + stroke_pixels
            fragments.append(pixels)

        return fragments

    def _clipping(self, fragments):
        fragments_clipped = []

        def is_in(p):
            content_width, content_height = self.size
            return p.x >= 0 and p.x < content_width and p.y >= 0 and p.y < content_height

        for pixels in fragments:
            pixels_clipped = [p for p in pixels if is_in(p)]
            fragments_clipped.append(pixels_clipped)

        return fragments_clipped

    def _fragment_processing(self, fragemnts):
        for pixels in fragemnts:
            for p in pixels:
                index = p.x + p.y * self.size[0]
                self.frame_buffer[index] = p.color

    def _scan_line_filling(self, polygon, fill_color):
        '''
        https://www.cs.uic.edu/~jbell/CourseNotes/ComputerGraphics/PolygonFilling.html
        '''

        # close the polygon
        polygon = polygon.copy()
        first = polygon[0]
        last = polygon[-1]
        if first.x != last.x or first.y != last.y:
            polygon.append(Point(first.x, first.y, first.color))

        pixels = []
        edges_horizontal = [(v, polygon[i + 1]) for i, v in enumerate(polygon)
                            if i < len(polygon) - 1 and v.y == polygon[i + 1].y]
        edges = [(v, polygon[i + 1])
                 for i, v in enumerate(polygon)
                 if i < len(polygon) - 1 and v.y != polygon[i + 1].y]
        ymin = min(polygon, key=lambda p: p.y).y
        ymax = max(polygon, key=lambda p: p.y).y

        def has_intersect(e, y):
            v1, v2 = e
            if v1.y > v2.y:
                return y <= v1.y and y > v2.y
            else:
                return y >= v1.y and y < v2.y

        for e in edges_horizontal:
            y = e[0].y
            x1 = min(e[0].x, e[1].x)
            x2 = max(e[0].x, e[1].x)
            for x in range(x1, x2 + 1):
                pixels.append(Point(x, y, fill_color))

        for y in range(ymin, ymax + 1):
            intersections = [round(map(y, e[0].y, e[1].y, e[0].x, e[1].x))
                             for e in edges if has_intersect(e, y)]
            if len(intersections) == 1:
                pixels += [Point(intersections[0], y, fill_color)]
            else:
                intersections_sorted = sorted(intersections)
                is_draw = True
                for i, x0 in enumerate(intersections_sorted):
                    if is_draw and i < len(intersections_sorted) - 1:
                        x1 = intersections_sorted[i + 1]
                        pixels += self._rasterize_line(
                            Point(x0, y, fill_color),
                            Point(x1, y, fill_color)
                        )
                    is_draw = not is_draw
        return pixels

    def _rasterize_line(self, v1, v2):
        pixels = []

        dx = abs(v1.x - v2.x)
        dy = abs(v1.y - v2.y)

        if dx >= dy:
            start_x = min(v1.x, v2.x)
            end_x = max(v1.x, v2.x)
            for x in range(start_x, end_x + 1):
                y = map(x, v1.x, v2.x, v1.y, v2.y)
                pixels += self._rasterize_point(
                    x, round(y),
                    v1.color,
                    v1.weight_x, v1.weight_y
                )
        else:
            start_y = min(v1.y, v2.y)
            end_y = max(v1.y, v2.y)
            for y in range(start_y, end_y + 1):
                x = map(y, v1.y, v2.y, v1.x, v2.x)
                pixels += self._rasterize_point(
                    round(x), y,
                    v1.color,
                    v1.weight_x, v1.weight_y
                )

        return pixels

    def _rasterize_ellipse(self, x0, y0, a, b):
        p1 = []
        p2 = []
        p3 = []
        p4 = []

        def is_in(x, y):
            return (b * x) ** 2 + (a * y) ** 2 - (a * b) ** 2 < 0

        def add_points(x, y, rx, ry):
            p1.append(Point(x, y))
            p2.append(Point(x, y + ry * 2))
            p3.append(Point(x - rx * 2, y + ry * 2))
            p4.append(Point(x - rx * 2, y))

        if a >= b:
            y = y0 - b
            for x in range(x0, x0 + a + 1):
                rx = x - x0
                ry = y0 - y
                add_points(x, y, rx, ry)
                if not is_in(rx + 1, ry - 0.5):
                    y += 1
            if y <= y0:
                add_points(x, y0, a, 0)
            p2 = list(reversed(p2))
            p4 = list(reversed(p4))
        else:
            x = x0 + a
            for y in range(y0, y0 + b + 1):
                rx = x - x0
                ry = y - y0
                add_points(x, y - ry * 2, rx, ry)
                if not is_in(rx - 0.5, ry + 1):
                    x -= 1
            if x >= x0:
                add_points(x0, y, 0, b)
            p1 = list(reversed(p1))
            p3 = list(reversed(p3))

        return p2 + p3 + p4 + p1

    def _rasterize_point(self, x, y, color, stroke_weight_x=0, stroke_weight_y=0):
        if stroke_weight_x == 0 and stroke_weight_y == 0:
            return [Point(x, y, color)]

        # draw circle
        points = self._rasterize_ellipse(
            x, y,
            stroke_weight_x, stroke_weight_y
        )

        for p in points:
            p.color = color

        # fill circle
        points += self._scan_line_filling(points, color)
        return points

    def _discretize_curve(self):
        pass

    def _discretize_bezier(self):
        pass

    def _discretize_arc(self):
        pass

    def _adjust_unicode_char(self):
        width, height = self.size
        flags = [0 for i in range(width)]
        wider_chars = []

        # scan the buffer to record unicode
        for i in range(height):
            wider_cnt = 0
            for j in range(width):
                index = j + i * width
                ch, _, _ = self.frame_buffer[index]
                ch_width = get_char_width(ch)
                if ch_width == 2:
                    flags[j] = 1
                    wider_cnt += 1
            wider_chars.append(wider_cnt)

        # insert and move the buffer
        for i in range(height):
            insert_indice = []
            for j in range(width):
                index = j + i * width
                color = self.frame_buffer[index]
                ch, _, _ = color
                ch_width = get_char_width(ch)
                if flags[j] == 1 and j < width - 1 and ch_width == 1:
                    insert_indice.append((index + 1, color))

            last_index = (i + 1) * width - 1
            while len(insert_indice):
                insert_index, color = insert_indice.pop()

                # change the count of wider chars if remove a wider char
                ch, _, _ = self.frame_buffer[last_index]
                ch_width = get_char_width(ch)
                if ch_width == 2:
                    wider_chars[i] -= 1

                # remove and insert
                self.frame_buffer.pop(last_index)
                self.frame_buffer.insert(insert_index, color)

            # remove chars exceed the screen
            wider_cnt = wider_chars[i]
            j = width - 1
            while wider_cnt > 0:
                index = j + i * width
                ch, _, _ = self.frame_buffer[index]
                self.frame_buffer[index] = None
                ch_width = get_char_width(ch)
                wider_cnt -= ch_width

                # it will remove more if the last one is wider char
                # in that case, wider_cnt == -1
                if wider_cnt == -1:
                    self.frame_buffer[index] = Color(" ")
                j -= 1

    def log_frame_buffer(self):
        width, height = self.size
        matrix = '\n'
        for i in range(height):
            line = ''
            for j in range(width):
                index = i * width + j
                color = self.frame_buffer[index]
                if not color:
                    line += 'n'
                    continue
                ch, _, _ = color
                if isinstance(ch, tuple):
                    ch, _ = ch
                s = "*" if ch == " " else ch
                line += s
            line += "\n"
            matrix += line
        logger.debug(matrix)


class Context(metaclass=ABCMeta):
    @ abstractclassmethod
    def open(self, size):
        """ open the drawing context"""

    @ abstractclassmethod
    def close(self):
        """ close the drawing context and restore state of canvas """

    @ abstractclassmethod
    def no_cursor(self):
        """ hide cursor """

    @ abstractclassmethod
    def cursor(self):
        """ show cursor """

    @ abstractclassmethod
    def get_events(self):
        """ get event: mouse event, keyboard event, cursor event """

    @ abstractclassmethod
    def draw(self, buffer):
        """ draw buffer to screen """

    @ abstractclassmethod
    def clear(self):
        """ clear the screen when called background() """


if sys.platform == "win32":
    class WindowsContext(Context):
        def open(self, size):
            print('hello windows context')

        def close(self):
            pass

        def no_cursor(self):
            pass

        def cursor(self):
            pass

        def get_events(self):
            pass

        def draw(self, buffer):
            pass

        def clear(self):
            pass


elif sys.platform == "brython":
    class BrowserContext(Context):

        def open(self, size):
            print('hello browser context')

        def close(self):
            pass

        def no_cursor(self):
            pass

        def cursor(self):
            pass

        def get_events(self):
            pass

        def draw(self, buffer):
            pass

        def clear(self, buffer):
            pass

else:
    import curses

    class CursesContext(Context):

        window_height = 0

        def __init__(self):
            self._screen = curses.initscr()
            self._screen.keypad(1)
            self._screen.nodelay(1)
            self.window_width = self._screen.getmaxyx()[1]
            self.window_height = self._screen.getmaxyx()[0]
            self._screen.leaveok(False)
            self._buffer = []
            self._color_pair = []

            curses.noecho()
            curses.cbreak()
            curses.start_color()  # Enables colors

            # Enable mouse events
            curses.mousemask(curses.ALL_MOUSE_EVENTS |
                             curses.REPORT_MOUSE_POSITION)

        def open(self, size):

            self._pad_width = size[0] + 2
            self._pad_height = size[1] + 2
            self._update_pad()

        def close(self):
            self._screen.keypad(0)
            curses.nocbreak()
            curses.echo()
            curses.endwin()

        def no_cursor(self):
            curses.curs_set(0)

        def cursor(self):
            curses.curs_set(1)

        def get_events(self):
            event_queue = []
            key = self._screen.getch()
            while key != -1:
                if key == curses.KEY_RESIZE:
                    self._resize()
                    event_queue.append(WindowEvent())
                elif key == curses.KEY_MOUSE:
                    _, x, y, _, bstate = curses.getmouse()
                    _x = x - (self._pad_x + 1)
                    _y = y - (self._pad_y + 1)
                    x_in = _x > 0 and _x < self._pad_width - 1
                    y_in = _y > 0 and _y < self._pad_width - 1
                    if x_in and y_in:
                        event_queue.append(MouseEvent(_x, _y, bstate))
                else:
                    # self._screen.move(10, 10)
                    event_queue.append(KeyboardEvent(key))
                key = self._screen.getch()
            return event_queue

        def draw(self, buffer, color_pair):
            self._buffer = buffer
            self._color_pair = color_pair
            self._enable_colors()
            wider_chars = self._count_wider_chars()

            for y in range(self._pad_height):
                for x in range(self._pad_width):
                    _x = x + self._pad_x
                    _y = y + self._pad_y
                    x_out = _x < 0 or _x > self.window_width - 2
                    y_out = _y < 0 or _y > self.window_height - 1
                    if x_out or y_out:
                        continue
                    border_ch = self._get_border(x, y)
                    if border_ch:
                        r = x == self._pad_width - 1 and y > 0 and y < self._pad_height - 1
                        if r:
                            cnt = wider_chars[y - 1]
                            self._screen.addstr(_y, _x - cnt,  border_ch)
                        else:
                            self._screen.addstr(_y, _x, border_ch)
                    else:
                        index = (x - 1) + (y - 1) * (self._pad_width - 2)
                        color = buffer[index]
                        if not color:
                            continue
                        ch, fg, bg = color
                        ch = ch[0] if isinstance(ch, tuple) else ch
                        color_index = self._get_color(fg, bg)

                        # It is strange that can't draw at (self.window_height - 1, self.window_width - 1)
                        self._screen.addstr(
                            _y, _x, ch, curses.color_pair(color_index))

            # update the physical sceen
            self._screen.refresh()

        def clear(self):
            self._screen.clear()

        def _count_wider_chars(self):
            wider_chars = []
            width = self._pad_width - 2
            height = self._pad_height - 2

            for i in range(height):
                wider_cnt = 0
                for j in range(width):
                    index = j + i * width
                    color = self._buffer[index]
                    if not color:
                        continue
                    ch, _, _ = color
                    ch_width = get_char_width(ch)
                    if ch_width == 2:
                        wider_cnt += 1
                wider_chars.append(wider_cnt)

            return wider_chars

        def _update_pad(self):
            self._pad_x = (self.window_width - self._pad_width) // 2
            self._pad_y = (self.window_height - self._pad_height) // 2

        def _enable_colors(self):
            for i, c in enumerate(self._color_pair):
                if not c[1]:
                    curses.init_pair(i + 1, c[0].fg, c[0].bg)
                    c[1] = True

        def _get_color(self, fg, bg):
            for i, color in enumerate(self._color_pair):
                c, _ = color
                if fg == c.fg and bg == c.bg:
                    return i + 1
            return 0

        def _get_border(self, x, y):
            lb = x == 0 and y == 0
            rb = x == self._pad_width - 1 and y == 0
            lt = x == 0 and y == self._pad_height - 1
            rt = x == self._pad_width - 1 and y == self._pad_height - 1
            b = y == 0 and x > 0 and x < self._pad_width - 1
            r = x == self._pad_width - 1 and y > 0 and y < self._pad_height - 1
            t = y == self._pad_height - 1 and x > 0 and x < self._pad_width - 1
            l = x == 0 and y > 0 and y < self._pad_height - 1

            if lb or rb or lt or rt:
                return "+"

            if b or t:
                return '-'

            if r or l:
                return '|'

            return None

        def _resize(self):
            curses.update_lines_cols()
            self.window_width = self._screen.getmaxyx()[1]
            self.window_height = self._screen.getmaxyx()[0]
            self._update_pad()
            self._screen.clear()
            self.draw(self._buffer, self._color_pair)


class CShape(object):

    def __init__(self, points=None, is_auto=True, primitive_type=constants.POLYGON, close_mode=constants.CLOSE, options=None):
        self.points = [] if points == None else points
        self.options = {} if options == None else options
        self.is_auto = is_auto
        self.primitive_type = primitive_type
        self.close_mode = close_mode
        self.fill_color = None
        self.stroke_color = None
        self.stroke_weight = None
        self.transform_matrix_stack = []
        self.is_stroke_enabled = True
        self.is_fill_enabled = True

    def __str__(self):
        attrs = {
            'fill_color': self.fill_color,
            'stroke_color': self.stroke_color,
            'primitive_type': self.primitive_type,
            'close_mode': self.close_mode,
            'is_stroke_enabled': self.is_stroke_enabled,
            'is_fill_enabled': self.is_fill_enabled,
            'stroke_weight': self.stroke_weight,
            'points': self.points
        }
        return attrs.__str__()

    __repr__ = __str__


class Point(object):

    def __init__(self, x, y, color=1, weight_x=0, weight_y=0, type="normal"):
        self.x = x
        self.y = y
        self.weight_x = weight_x
        self.weight_y = weight_y
        self.color = color
        self.type = type

    def __str__(self):
        attrs = {
            "x": self.x,
            "y": self.y,
            "weight_x": self.weight_x,
            "weight_y": self.weight_y,
            "color": self.color
        }
        return attrs.__str__()

    def __eq__(self, other):
        x = self.x == other.x
        y = self.y == other.y
        weight_x = self.weight_x == other.weight_x
        weight_y = self.weight_y == other.weight_y
        color = self.color == other.color
        type = self.type == other.type
        return x and y and weight_x and weight_y and color and type

    def __hash__(self):
        return hash('(%s, %s)' % (self.x, self.y))

    __repr__ = __str__


class Color(object):

    def __init__(self, ch=" ", fg=constants.WHITE, bg=constants.BLACK):
        self.index = 0

        if isinstance(ch, self.__class__):
            self.ch = ch.ch
            self.fg = ch.fg
            self.bg = ch.bg
        else:
            self.ch = ch
            self.fg = fg
            self.bg = bg

            self.fg = constants.WHITE if self.fg == None else self.fg
            self.bg = constants.BLACK if self.bg == None else self.bg

            # solve the display problem when ch == " " and fg == WHITE
            # self.fg = BLACK if ch == " " else self.fg

        # add to color pair
        if not self.has_color(self.fg, self.bg, Renderer.color_pair):
            Renderer.color_pair.append([self, False])

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 2:
            self.index = 0
            raise StopIteration()
        attrs = [self.ch, self.fg, self.bg]
        a = attrs[self.index]
        self.index += 1
        return a

    def has_color(self, fg, bg, color_pair):
        equal_colors = [
            color for color, enable in color_pair
            if color.fg == fg and color.bg == bg
        ]
        return len(equal_colors) > 0

    def __str__(self):
        attrs = {
            "ch": self.ch,
            "fg": self.fg,
            "bg": self.bg
        }
        return attrs.__str__()

    __repr__ = __str__


class CImage(object):
    pass


class ImageLoader(object):
    pass


class Event(object):
    type = ""

    def __init__(self, type):
        self.type = type


class WindowEvent(Event):
    def __init__(self):
        super(WindowEvent, self).__init__('window')


class MouseEvent(Event):
    mouse_type = ""

    def __init__(self, x, y, type):
        super(MouseEvent, self).__init__('mouse')
        self.x = x
        self.y = y
        self.mouse_type = type


class KeyboardEvent(Event):

    def __init__(self, key):
        super(KeyboardEvent, self).__init__('keyboard')
        self.key = key
