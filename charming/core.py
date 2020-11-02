import time
import logging
import sys
import math
from abc import ABCMeta, abstractclassmethod
from . import constants
from .cmath import map
from .cmath import dist
from .utils import Matrix
from .utils import angle_between
from .utils import get_char_width
from .utils import to_left

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
        self.has_setup_hook = False
        self.has_draw_hook = False
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
            is_static_mode = not self.has_draw_hook or not self.has_setup_hook
            if is_static_mode:
                self.context.open(self.size)
                self.renderer.setup(self.size)
                self.renderer.render()
                self.context.draw(self.renderer.frame_buffer,
                                  self.renderer.color_pair)
                if self.is_log_frame_buffer == True:
                    self.renderer.log_frame_buffer()
                while True:
                    events = self.context.get_events()
                    for e in events:
                        if e.type == "window":
                            self._handle_event(e)
                    time.sleep(1)
            else:
                setup_hook = self.hooks_map['setup']
                draw_hook = self.hooks_map['draw']
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
        self.frame_buffer = [Color(' ')
                             for _ in range(width * height)
                             ]

    def _render_shape(self, shape):

        vertices = self._vertex_processing(
            shape.points,
            shape.stroke_color,
            shape.stroke_weight,
            shape.transform_matrix_stack)

        primitives = self._primitive_assembly(
            vertices,
            shape.primitive_type,
            shape.close_mode,
            shape.options)

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
        rotation = 0
        while len(transform_matrix_stack) > 0:
            matrix = transform_matrix_stack.pop()
            tm = matrix * tm
            if matrix.type == "scale":
                sm = matrix * sm
            elif matrix.type == "rotate":
                rotation += matrix.value
        sx = sm[0][0]
        sy = sm[1][1]

        for p in points:
            mp = Matrix([[p.x], [p.y], [1]])
            tp = tm * mp
            p.x = tp[0][0]
            p.y = tp[1][0]
            p.weight_x = sx * stroke_weight if stroke_weight != 0 else sx - 1
            p.weight_y = sy * stroke_weight if stroke_weight != 0 else sy - 1
            p.rotation = rotation

        # screen map && color
        for p in points:
            p.color = stroke_color
            p.x = round(p.x)
            p.y = round(p.y)

        return points

    def _primitive_assembly(self, vertices, primitive_type, close_mode, options):
        # vertices
        if primitive_type == constants.POLYGON:
            if close_mode == constants.CLOSE:
                normal_vertices = [v for v in vertices if v.type == "normal"]
                vertices.append(normal_vertices[0])
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
            start = options['start']
            stop = options['stop']
            mode = options['mode']
            p1, p2, p3, p4 = vertices
            a = int(dist(p1.x, p1.y, p2.x, p2.y) / 2)
            b = int(dist(p1.x, p1.y, p4.x, p4.y) / 2)
            x0 = int((p1.x + p3.x) / 2)
            y0 = int((p1.y + p3.y) / 2)
            rotation = angle_between(1, 0, p2.x - p1.x, p2.y - p1.y)
            points = self._discretize_arc(
                x0, y0, a, b, start, stop, p1.color, rotation, mode
            )
            ps = [points]
        elif primitive_type == constants.CURVE:
            points = []
            curve_tightness = options['curve_tightness']
            for i, v in enumerate(vertices):
                if i < len(vertices) - 3:
                    points += self._discretize_curve(
                        v, vertices[i + 1], vertices[i + 2], vertices[i + 3],
                        v.color,
                        curve_tightness
                    )
            ps = [points]
        elif primitive_type == constants.BEZIER:
            points = []
            for i, v in enumerate(vertices):
                if i < len(vertices) - 3 and i % 3 == 0:
                    points += self._discretize_bezier(
                        v, vertices[i + 1], vertices[i + 2], vertices[i + 3],
                        v.color
                    )
            ps = [points]

        # edges
        edges_list = []
        for vertices in ps:
            unique_vertices = [v for i, v in enumerate(vertices)
                               if i == 0 or
                               (v.x != vertices[i - 1].x or
                                v.y != vertices[i - 1].y)
                               ]
            normal_vertices = [v for v in unique_vertices if v.type == "normal"]
            contour_vertices = [v for v in unique_vertices if v.type == "contour"]
            normal_edges = self._vertices_to_edges(normal_vertices)
            contour_edges = self._vertices_to_edges(contour_vertices)
            edges_list.append(normal_edges + contour_edges)

        return edges_list

    def _rasterization(self, primitives, fill_color, is_stroke_enabled, is_fill_enabled):
        fragments = []

        for edges in primitives:
            fill_pixels = []
            stroke_pixels = []

            if len(edges) == 0:
                fragments.append([])
            elif len(edges) == 1:
                e = edges[0]
                if len(e) == 1:
                    stroke_pixels += self._rasterize_point(
                        e[0].x, e[0].y,
                        e[0].color,
                        e[0].weight_x, e[0].weight_y,
                        e[0].rotation
                    )
                else:
                    stroke_pixels += self._rasterize_line(e[0], e[1])
                fragments.append(stroke_pixels)
            else:
                # fill polygon
                if is_fill_enabled:
                    # close the polygon
                    fill_edges = edges.copy()
                    normal_edges = [
                        e for e in fill_edges
                        if e[0].type == "normal"
                    ]
                    first_point = normal_edges[0][0]
                    last_point = normal_edges[-1][1]
                    if last_point.x != first_point.x or last_point.y != first_point.y:
                        fill_edges.append((last_point, first_point))
                    fill_pixels += self._scan_line_filling(
                        fill_edges, fill_color)

                # stroke the polygon
                if is_stroke_enabled:
                    for _, e in enumerate(edges):
                        stroke_pixels += self._rasterize_line(
                            e[0],
                            e[1],
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
        pixels = []
        ymin = float('inf')
        ymax = float('-inf')
        for e in polygon:
            v1, v2 = e
            ymin = min(v1.y, v2.y, ymin)
            ymax = max(v1.y, v2.y, ymax)

        def has_intersect(e, y):
            v1, v2 = e
            if v1.y > v2.y:
                return y < v1.y and y >= v2.y
            elif v1.y == v2.y:
                return y == v1.y
            else:
                return y > v1.y and y <= v2.y

        for y in range(ymin, ymax + 1):
            # calc the intersections
            intersections = []
            for i, e in enumerate(polygon):
                if has_intersect(e, y):
                    v1, v2 = e
                    if v1.y == v2.y:
                        x = v2.x
                    else:
                        x = round(map(y, v1.y, v2.y, v1.x, v2.x))

                    # pay more attention if is a joint point
                    ne = polygon[i + 1] if i < len(polygon) - 1 else polygon[0]
                    v3 = ne[1]
                    y_diff = (v1.y - y) * (v3.y - y)
                    is_left = to_left(v1.x, v1.y, v2.x, v2.y, v3.x, v3.y)
                    is_joint = x == v2.x and y == v2.y
                    if is_joint and (y_diff > 0 or (y_diff == 0 and is_left)):
                        intersections += [x, x]
                    else:
                        intersections += [x]

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
                    v1.weight_x, v1.weight_y,
                    v1.rotation
                )
        else:
            start_y = min(v1.y, v2.y)
            end_y = max(v1.y, v2.y)
            for y in range(start_y, end_y + 1):
                x = map(y, v1.y, v2.y, v1.x, v2.x)
                pixels += self._rasterize_point(
                    round(x), y,
                    v1.color,
                    v1.weight_x, v1.weight_y,
                    v1.rotation
                )

        return pixels

    def _rasterize_point(self, x, y, color, stroke_weight_x=0, stroke_weight_y=0, rotation=0):
        if stroke_weight_x == 0 or stroke_weight_y == 0:
            return [Point(x, y, color)]

        vertices = self._discretize_arc(
            x, y,
            stroke_weight_x,
            stroke_weight_y,
            0,
            constants.TAU,
            color,
            rotation
        )
        edges = self._vertices_to_edges(vertices)
        return self._scan_line_filling(edges, color)

    def _discretize_arc(self, x0, y0, a, b, start, stop, color, rotation=0, mode=constants.CHORD):
        if a == 0 or b == 0:
            return [Point(x0, y0, color)]

        points = []
        pre_x = a
        pre_y = 0
        pre_angle = 0
        angle = start
        cs = (2 * math.pi * b + 4 * (a - b)) * (stop - start) / (math.pi * 2)
        cnt = max(10, int(cs / 20) * 10)
        step = (stop - start) / cnt

        while angle < stop or math.isclose(angle, stop, abs_tol=1e-9):
            theta = angle - pre_angle
            pre_angle = angle
            angle += step

            cos = math.cos(theta)
            sin = math.sin(theta)

            x = pre_x * cos + pre_y * sin * (-a / b)
            y = pre_x * sin * (b / a) + pre_y * cos
            if x != pre_x or y != pre_y:
                pre_x = x
                pre_y = y

                rotated_x = math.cos(rotation) * x - math.sin(rotation) * y
                rotated_y = math.sin(rotation) * x + math.cos(rotation) * y
                points.append(Point(round(rotated_x + x0),
                                    round(rotated_y + y0),
                                    color=color)
                              )
        if mode == constants.PIE:
            points.insert(0, Point(x0, y0, color=color))
            points.append(points[0])
        elif mode == constants.CHORD:
            points.append(points[0])

        return points

    def _discretize_curve(self, p0, p1, p2, p3, color, s):
        t = 0
        d = dist(p1.x, p1.y, p2.x, p2.y)
        cnt = int(d / 2)
        points = []
        pre_x = None
        pre_y = None
        s = 1 - s
        while t < 1 or math.isclose(t, 1, abs_tol=1e-9):
            t3 = t ** 3
            t2 = t ** 2
            t1 = t
            t0 = 1
            a = -s * t3 + 2 * s * t2 - s * t1
            b = (2 - s) * t3 + (s - 3) * t2 + 1 * t0
            c = (s - 2) * t3 + (3 - 2 * s) * t2 + s * t1
            d = s * t3 - s * t2
            x = round(a * p0.x + b * p1.x + c * p2.x + d * p3.x)
            y = round(a * p0.y + b * p1.y + c * p2.y + d * p3.y)
            if pre_x != x or pre_y != y:
                points.append(Point(x, y, color=color))
            pre_x = x
            pre_y = y
            t += 1 / cnt
        return points

    def _discretize_bezier(self, p0, p1, p2, p3, color):
        t = 0
        d1 = dist(p0.x, p0.y, p1.x, p1.y)
        d2 = dist(p1.x, p1.y, p2.x, p2.y)
        d3 = dist(p2.x, p2.y, p3.x, p3.y)
        cnt = int((d1 + d2 + d3) / 3)
        points = []
        pre_x = None
        pre_y = None
        while t < 1 or math.isclose(t, 1, abs_tol=1e-9):
            a = (1 - t) ** 3
            b = 3 * t * (1 - t) ** 2
            c = 3 * t ** 2 * (1 - t)
            d = t ** 3
            x = round(a * p0.x + b * p1.x + c * p2.x + d * p3.x)
            y = round(a * p0.y + b * p1.y + c * p2.y + d * p3.y)
            if pre_x != x or pre_y != y:
                points.append(Point(x, y, color=color))
            pre_x = x
            pre_y = y
            t += 1 / cnt
        return points

    def _vertices_to_edges(self, vertices):
        if len(vertices) == 0:
            return []
        elif len(vertices) == 1:
            v = vertices[0]
            return [(v,)]
        else:
            edges = []
            for i in range(1, len(vertices)):
                v1 = vertices[i - 1]
                v2 = vertices[i]
                edges.append((v1, v2))
            return edges

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

    def __init__(self, x, y, color=1, weight_x=0, weight_y=0, rotation=0, type="normal"):
        self.x = x
        self.y = y
        self.weight_x = weight_x
        self.weight_y = weight_y
        self.color = color
        self.type = type
        self.rotation = rotation

    def __str__(self):
        attrs = {
            "x": self.x,
            "y": self.y,
            # "weight_x": self.weight_x,
            # "weight_y": self.weight_y,
            # "color": self.color
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
