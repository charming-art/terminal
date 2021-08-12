import sys
import math
import colorsys
import string
import time
from abc import ABCMeta, abstractclassmethod
from pyfiglet import Figlet
from . import constants

from .globals import WINDOWS
from .globals import POSIX

from .utils import map
from .utils import dist
from .utils import Matrix
from .utils import angle_between
from .utils import get_char_width
from .utils import to_left
from .utils import logger
from .utils import list_find


class Sketch(object):

    def __init__(self, renderer, context):
        self.renderer = renderer
        self.context = context
        self.timer = LocalTimer()

        self.frame_rate = 30
        self.is_loop = True
        self.is_draw = False
        self.should_exit = False
        self.frame_count = 0

        self.key = None
        self.key_code = None

        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_button = constants.NONE
        self.is_mouse_pressed = False

        self.has_setup_hook = False
        self.has_draw_hook = False

        self._check_params = False
        self.hooks_map = {
            'setup': lambda: None,
            'draw': lambda: None,
            'mouse_clicked': lambda: None,
            'mouse_pressed': lambda: None,
            'mouse_released': lambda: None,
            'key_pressed': lambda: None,
            'key_typed': lambda: None,
            'key_released': lambda: None,
            'window_resized': lambda: None,
            'cursor_moved': lambda: None,
            'cursor_pressed': lambda: None,
        }

        self.cursor_moved = False

    def run(self):
        try:
            if self.has_setup_hook:
                self._run_hook('setup')

            if not self.context.has_open:
                raise Exception(
                    'Call size() or full_screen() to open context.'
                )
            else:
                self._setup()
                self._loop()
                if self.has_draw_hook and self.has_setup_hook:
                    self.timer.run(1000 / self.frame_rate, self._loop)
                elif not self.should_exit:
                    self.timer.wait()
        except Exception as e:
            logger.debug(e)
            raise e
        finally:
            self.context.exit()
            self.context.close()
            logger.log_record()

    def add_hook(self, name, hook):
        self.hooks_map[name] = hook

    @logger.record('setup')
    def _setup(self):
        self.context.init()
        self.renderer.setup(self.context.width, self.context.height)
        self.context.background(
            self.renderer.background_color,
            self.renderer.mode
        )

    @logger.record('loop')
    def _loop(self):
        _is_draw = self.is_draw
        _is_loop = self.is_loop

        # draw hook
        if _is_loop or _is_draw:
            if self.has_draw_hook:
                self._run_hook('draw')

        # handle events
        events = self.context.get_events()
        self._handle_events(events)

        # render
        if _is_loop or _is_draw:
            self.renderer.render()
            self.context.draw(
                self.renderer.update_cells,
                self.renderer.mode,
            )

            self.renderer.has_background_called = False
            self.frame_count += 1

        if _is_draw:
            self.is_draw = False

        return self.should_exit

    def _run_hook(self, key):
        hook = self.hooks_map[key]
        hook()
        self.renderer.clear_matrix_stack()

    def _handle_events(self, events):
        pressed = False

        for e in events:
            if e.type == 'mouse':
                self.mouse_x = e.x
                self.mouse_y = e.y
                self.mouse_button = e.button_type
                if e.event_type == "pressed":
                    self.is_mouse_pressed = True
                    self._run_hook('mouse_pressed')
                elif e.event_type == "clicked":
                    self._run_hook('mouse_clicked')
                elif e.event_type == "released":
                    self.is_mouse_pressed = False
                    self._run_hook('mouse_released')
            elif e.type == "window":
                if e.event_type == "start":
                    self._run_hook('window_resized')
                elif e.event_type == "end":
                    self.renderer.clear()
                    self.context.restore(
                        self.renderer.frame_buffer,
                        self.renderer.mode
                    )
            elif e.type == "keyboard":
                self.key = e.key
                self.key_code = e.key_code
                if e.event_type == "pressed":
                    pressed = True
                    self._run_hook('key_pressed')
                    if self.key == constants.CODED:
                        if self.key_code == constants.UP:
                            self.context.move_up()
                            self._run_hook('cursor_moved')
                            self.cursor_moved = True
                        elif self.key_code == constants.DOWN:
                            self.context.move_down()
                            self._run_hook('cursor_moved')
                            self.cursor_moved = True
                        elif self.key_code == constants.LEFT:
                            self.context.move_left()
                            self._run_hook('cursor_moved')
                            self.cursor_moved = True
                        elif self.key_code == constants.RIGHT:
                            self.context.move_right()
                            self._run_hook('cursor_moved')
                            self.cursor_moved = True
                        else:
                            self.cursor_moved = False
                    else:
                        self.cursor_moved = False
                elif e.event_type == "typed":
                    self._run_hook('key_typed')
                elif e.event_type == "released":
                    self._run_hook('key_released')
                    self.cursor_moved = False

        if self.context.key_pressed and self.cursor_moved:
            self._run_hook('cursor_pressed')

        if self.context.key_pressed and not pressed:
            self._run_hook('key_pressed')


class Renderer(object):

    def __init__(self):
        self._flag = True
        self._color_by_pos = {}
        self._pre_color_by_pos = {}
        self._shape_queue = []
        self.update_cells = []

        # styles
        self.color_channels = (255,)
        self.stroke_weight = 0
        self.is_stroke_enabled = True
        self.is_fill_enabled = True
        self.is_tint_enabled = False
        self.rect_mode = constants.CORNER
        self.ellipse_mode = constants.CENTER
        self.image_mode = constants.CORNER
        self.text_align_x = constants.LEFT
        self.text_align_y = constants.TOP
        self.text_size = constants.NORMAL
        self.text_font = 'standard'

        self.has_background_called = False
        self.transform_matrix_stack = []
        self.width = 10
        self.height = 10

    def init(self, mode):
        self.fill_color = Color(' ')
        self.background_color = Color(' ')
        self.pre_background_color = Color(' ')
        self.stroke_color = Color('*')
        self.tint_color = Color('·')
        self.mode = mode

    def setup(self, width, height):
        self.width = width
        self.height = height
        self.frame_buffer = [
            self.background_color for _ in range(width * height)
        ]

    def render(self):
        self.update_cells.clear()
        self._color_by_pos = {}
        while len(self._shape_queue) > 0:
            shape = self._shape_queue.pop(0)
            self._render_shape(shape)
        self._differ_buffer()
        self.clear_matrix_stack()

    def clear_matrix_stack(self):
        self.transform_matrix_stack.clear()

    def clear(self):
        self._pre_color_by_pos = {}

    def add_element(self, element):
        try:
            if isinstance(element, Image):
                element = element.to_shape()
            elif isinstance(element, Text):
                element = element.to_shape(
                    self.text_size,
                    self.text_font,
                    self.text_align_x,
                    self.text_align_y
                )
            if element.is_auto:
                element.fill_color = self.fill_color
                element.stroke_color = self.stroke_color
                element.tint_color = self.tint_color
                element.stroke_weight = self.stroke_weight
                element.is_tint_enabled = self.is_tint_enabled
                element.is_fill_enabled = self.is_fill_enabled
                element.is_stroke_enabled = self.is_stroke_enabled
                element.transform_matrix_stack = self.transform_matrix_stack[:]
            self._shape_queue.append(element)
        except Exception as e:
            print('Call size() or full_screen() to open context.')
            raise e

    def background(self, color):
        self.has_background_called = True
        self.pre_background_color = self.background_color
        self.background_color = color
        self.frame_buffer = [
            color for i in range(self.width * self.height)
        ]

    @logger.record('render shape')
    def _render_shape(self, shape):
        vertices = self._vertex_processing(
            shape.points,
            shape.stroke_color,
            shape.tint_color,
            shape.is_tint_enabled,
            shape.stroke_weight,
            shape.transform_matrix_stack,
            shape.primitive_type
        )

        primitives = self._primitive_assembly(
            vertices,
            shape.primitive_type,
            shape.close_mode,
            shape.options
        )

        fragments = self._rasterization(
            primitives,
            shape.fill_color,
            shape.tint_color,
            shape.is_stroke_enabled,
            shape.is_fill_enabled,
            shape.primitive_type
        )

        fragments_clipped = self._clipping(
            fragments,
            shape.primitive_type
        )

        self._fragment_processing(fragments_clipped)

    @logger.record('vertex processing')
    def _vertex_processing(
        self,
        points,
        stroke_color,
        tint_color,
        is_tint_enabled,
        stroke_weight,
        transform_matrix_stack,
        primitive_type
    ):
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
            # transform
            mp = Matrix([[p.x], [p.y], [1]])
            tp = tm * mp
            p.x = int(tp[0][0])
            p.y = int(tp[1][0])
            p.weight_x = sx * stroke_weight if stroke_weight != 0 else sx - 1
            p.weight_y = sy * stroke_weight if stroke_weight != 0 else sy - 1
            p.rotation = rotation

            # screen map && color
            if primitive_type == constants.IMAGE:
                if is_tint_enabled:
                    ch = tint_color.ch
                    fg = tint_color.fg
                else:
                    ch = p.color.ch
                    fg = p.color.fg
                p.color = Color.create(ch, fg, p.color.bg)
            elif primitive_type == constants.TEXT:
                p.color = Color.create(
                    p.color.ch,
                    stroke_color.fg,
                    stroke_color.bg
                )
            else:
                p.color = stroke_color

        return points

    @logger.record('primitive assembly')
    def _primitive_assembly(
        self,
        vertices,
        primitive_type,
        close_mode,
        options
    ):
        # vertices
        if primitive_type == constants.POLYGON:
            if close_mode == constants.CLOSE:
                normal_vertices = [
                    v for v in vertices
                    if v.type == "normal"
                ]
                vertices.append(normal_vertices[0])
            ps = [vertices]
        elif primitive_type == constants.POINTS:
            ps = [[v] for v in vertices]
        elif primitive_type == constants.LINES:
            ps = [
                [vertices[i],
                 vertices[i + 1]]
                for i in range(0, len(vertices) - 1, 2)
            ]
        elif primitive_type == constants.TRIANGLES:
            ps = [
                [vertices[i],
                 vertices[i + 1],
                 vertices[i + 2],
                 vertices[i]]
                for i in range(0, len(vertices) - 2, 3)
            ]
        elif primitive_type == constants.TRIANGLE_STRIP:
            ps = [
                [vertices[i],
                 vertices[i + 1],
                 vertices[i + 2],
                 vertices[i]]
                for i in range(len(vertices) - 2)
            ]
        elif primitive_type == constants.TRIANGLE_FAN:
            ps = [
                [vertices[0],
                 vertices[i],
                 vertices[i + 1],
                 vertices[0]]
                for i in range(1, len(vertices) - 1)
            ]
        elif primitive_type == constants.QUADS:
            ps = [
                [vertices[i],
                 vertices[i + 1],
                 vertices[i + 2],
                 vertices[i + 3],
                 vertices[i]]
                for i in range(0, len(vertices) - 3, 4)
            ]
        elif primitive_type == constants.QUAD_STRIP:
            ps = [
                [vertices[i],
                 vertices[i + 1],
                 vertices[i + 3],
                 vertices[i + 2],
                 vertices[i]]
                for i in range(0, len(vertices) - 3, 2)
            ]
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
            for i in range(len(vertices) - 3):
                points += self._discretize_curve(
                    vertices[i],
                    vertices[i + 1],
                    vertices[i + 2],
                    vertices[i + 3],
                    vertices[i].color,
                    curve_tightness
                )
            ps = [points]
        elif primitive_type == constants.BEZIER:
            points = []
            for i in range(0, len(vertices) - 3, 3):
                points += self._discretize_bezier(
                    vertices[i],
                    vertices[i + 1],
                    vertices[i + 2],
                    vertices[i + 3],
                    vertices[i].color
                )
            ps = [points]
        elif primitive_type == constants.IMAGE:
            w = options['width']
            h = options['height']
            ps = []
            for j in range(h):
                for i in range(w):
                    w1 = w + 1
                    i1 = j * w1 + i
                    i2 = j * w1 + i + 1
                    i3 = (j + 1) * w1 + i + 1
                    i4 = (j + 1) * w1 + i
                    v_list = [
                        vertices[i1], vertices[i2],
                        vertices[i4], vertices[i3]
                    ]
                    index_visible = list_find(v_list, lambda x: x.visible)
                    if index_visible != -1:
                        v = v_list[index_visible]
                        ps.append([v] * 4)

        elif primitive_type == constants.TEXT:
            ps = [[v] for v in vertices]

        # edges
        edges_list = []
        for vertices in ps:
            unique_vertices = [
                v for i, v in enumerate(vertices)
                if i == 0
                or (v.x != vertices[i - 1].x or v.y != vertices[i - 1].y)
            ]
            normal_vertices = [
                v for v in unique_vertices
                if v.type == "normal"
            ]
            contour_vertices = [
                v for v in unique_vertices
                if v.type == "contour"
            ]
            normal_edges = self._vertices_to_edges(normal_vertices)
            contour_edges = self._vertices_to_edges(contour_vertices)
            edges_list.append(normal_edges + contour_edges)

        return edges_list

    @logger.record('rasterizatioin')
    def _rasterization(
        self,
        primitives,
        fill_color,
        tint_color,
        is_stroke_enabled,
        is_fill_enabled,
        primitive_type
    ):
        fragments = []
        is_image = primitive_type == constants.IMAGE
        is_text = primitive_type == constants.TEXT

        for edges in primitives:
            fill_pixels = []
            stroke_pixels = []

            if len(edges) == 0:
                fragments.append([])
            elif len(edges) == 1:
                if is_stroke_enabled:
                    stroke_pixels += self._rasterize_line(
                        edges[0][0],
                        edges[0][-1]
                    )
                    fragments.append(stroke_pixels)
            else:
                # fill polygon
                if is_fill_enabled:
                    fill_edges = self._close_polygon(edges)

                    if is_image or is_text:
                        fill_color = fill_edges[0][0].color

                    fill_pixels += self._scan_line_filling(
                        fill_edges,
                        fill_color
                    )

                # stroke the polygon
                if is_stroke_enabled and not is_image:
                    for e in edges:
                        stroke_pixels += self._rasterize_line(
                            e[0],
                            e[1],
                        )

                pixels = fill_pixels + stroke_pixels
                fragments.append(pixels)
        return fragments

    @logger.record('clipping')
    def _clipping(self, fragments, primitive_type):
        fragments_clipped = []
        scale = 2 if self.mode == constants.DOUBLE else 1
        need_wrap = primitive_type == constants.TEXT and self.mode == constants.DOUBLE

        for pixels in fragments:
            pixels_clipped = []
            for p in pixels:
                p.x *= scale
                if p.x >= 0 and p.x < self.width and p.y >= 0 and p.y < self.height:
                    # process text character
                    if need_wrap:
                        ch = p.color.ch
                        ch_w = get_char_width(ch)
                        ch = ch[0] if isinstance(ch, tuple) else ch
                        if ch_w == 1:
                            p.color.ch = (ch, 2)
                    pixels_clipped.append(p)
            fragments_clipped.append(pixels_clipped)

        return fragments_clipped

    @logger.record('fragment processing')
    def _fragment_processing(self, fragments):
        for pixels in fragments:
            for p in pixels:
                key = f'({p.x},{p.y})'
                index = p.y * self.width + p.x
                self._color_by_pos[key] = [p, self._flag]
                self.frame_buffer[index] = p.color

    @logger.record('differ buffer')
    def _differ_buffer(self):
        update_colors = self._color_by_pos.copy()

        # remove
        remove_keys = []
        for key, value in update_colors.items():
            if key in self._pre_color_by_pos:
                self._pre_color_by_pos[key][1] = self._flag
                pvalue = self._pre_color_by_pos[key]
                if pvalue[0] == value[0]:
                    remove_keys.append(key)

        for key in remove_keys:
            update_colors.pop(key)

        # add
        if self.has_background_called:
            keys = [
                key for key, value in self._pre_color_by_pos.items()
                if value[1] != self._flag
            ]
            for key in keys:
                pp = self._pre_color_by_pos[key][0]
                if pp.color != self.background_color:
                    update_colors[key] = [
                        Point(pp.x, pp.y, self.background_color),
                        pp, self._flag
                    ]

            if self.background_color != self.pre_background_color:
                for x in range(self.width):
                    for y in range(self.height):
                        key = f'({x},{y})'
                        if not key in self._color_by_pos and not key in update_colors:
                            update_colors[key] = [
                                Point(x, y, self.background_color),
                                self._flag
                            ]

        self.update_cells = [value[0] for value in update_colors.values()]
        self._pre_color_by_pos = self._color_by_pos
        self._flag = not self._flag

    @logger.record('polygon filling')
    def _scan_line_filling(self, polygon, fill_color):
        pixels = []
        ymin = float('inf')
        ymax = float('-inf')
        for e in polygon:
            v1 = e[0]
            v2 = e[1]
            ymin = min(v1.y, v2.y, ymin)
            ymax = max(v1.y, v2.y, ymax)

        def has_intersect(e, y):
            v1 = e[0]
            v2 = e[1]
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
                    v1, v2, v3 = e
                    if v1.y == v2.y:
                        x = v2.x
                    else:
                        x = round(map(y, v1.y, v2.y, v1.x, v2.x))

                    # pay more attention if is a joint point
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

    @logger.record('draw line')
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

    def _rasterize_point(
        self,
        x,
        y,
        color,
        stroke_weight_x=0,
        stroke_weight_y=0,
        rotation=0
    ):
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

    def _discretize_arc(
        self,
        x0,
        y0,
        a,
        b,
        start,
        stop,
        color,
        rotation=0,
        mode=constants.CHORD
    ):
        if a == 0 or b == 0:
            return [Point(x0, y0, color)]

        points = []
        pre_x = a
        pre_y = 0
        pre_angle = 0
        angle = start
        cs = (2 * math.pi * b + 4 * (a - b)) * \
            (stop - start) / (math.pi * 2)
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

            if x != pre_x or y != pre_y or len(points) == 0:
                pre_x = x
                pre_y = y
                rotated_x = math.cos(rotation) * x - math.sin(rotation) * y
                rotated_y = math.sin(rotation) * x + math.cos(rotation) * y
                points.append(
                    Point(
                        round(rotated_x + x0),
                        round(rotated_y + y0),
                        color=color
                    )
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

    def _vertices_to_edges(self, vertices, clockwise=True):
        if len(vertices) == 0:
            return []
        elif len(vertices) == 1:
            v = vertices[0]
            return [(v,)]
        elif len(vertices) == 2:
            v1 = vertices[0]
            v2 = vertices[-1]
            return [(v1, v2)]
        else:
            if clockwise != self._is_clockwise(vertices):
                vertices = list(reversed(vertices))
            edges = []
            vl = len(vertices)
            v0 = vertices[0]
            for i in range(vl - 1):
                v1 = vertices[i]
                v2 = vertices[(i + 1) % vl]
                v3 = vertices[(i + 2) % vl]
                if v3.x == v0.x and v3.y == v0.y:
                    v3 = vertices[(i + 3) % vl]
                edges.append((v1, v2, v3))

            return edges

    def _close_polygon(self, edges, type="normal"):
        fill_edges = edges.copy()
        normal_edges = [
            e for e in fill_edges
            if e[0].type == type
        ]
        p1 = normal_edges[0][0]
        p2 = normal_edges[0][1]
        pe = normal_edges[-1][1]
        if pe.x != p1.x or pe.y != p1.y:
            fill_edges.append((pe, p1, p2))
        return fill_edges

    def _is_clockwise(self, vertices):
        signed_area = 0
        vl = len(vertices)
        for i in range(vl):
            v0 = vertices[i]
            v1 = vertices[(i + 1) % vl]
            signed_area += v0.x * v1.y - v1.x * v0.y
        return signed_area > 0


class Context(metaclass=ABCMeta):

    @abstractclassmethod
    def close(self):
        """ close the drawing context and restore state of canvas """

    @abstractclassmethod
    def get_events(self):
        """ get event: mouse event, keyboard event, cursor event """

    @abstractclassmethod
    def init(self):
        """ init the terminal """

    @abstractclassmethod
    def background(self, color, mode):
        ''' set the backgroun color of the terminal '''

    @abstractclassmethod
    def get_window_size(self):
        ''' get the terminal window size '''
        pass

    @abstractclassmethod
    def _update_window_size(self):
        """ update the size of the window """

    def __init__(self):
        self.inner_width = 0
        self.inner_height = 0

        self.terminal_width = 0
        self.terminal_height = 0

        self.window_width = 0
        self.window_height = 0

        self.width = 0
        self.height = 0

        self.key_pressed = False

        self.cursor_x = 0
        self.cursor_y = 0
        self.pcursor_x = 0
        self.pcursor_y = 0

        self._pad_x = 0
        self._pad_y = 0
        self._pad_width = 0
        self._pad_height = 0

        self.has_open = False
        self._has_cursor = True
        self._has_background = False
        self._screen = None

        self._content = ""

    def open(self, width=10, height=10, is_full_screen=False):
        self.has_open = True

        if is_full_screen:
            self.width = self.window_width
            self.height = self.window_height
        else:
            self.width = width
            self.height = height

        self._pad_width = self.width + 2
        self._pad_height = self.height + 2
        self._pad_x = (self.window_width - self._pad_width) // 2
        self._pad_y = (self.window_height - self._pad_height) // 2

    @logger.record('flush screen')
    def draw(self, points, mode):
        self._draw_background()
        self._draw_border()
        self._content = ''

        for p in points:
            x = p.x + self._pad_x + 1
            y = p.y + self._pad_y + 1
            if self._in(x, y):
                ch = self._ch(p.color.ch, mode)
                self._addch(x, y, ch, p.color.fg, p.color.bg)

        self._draw_cursor()
        self._refresh()

    def restore(self, frame_buffer, mode):
        self._draw_border()
        self._content = ''

        for i, color in enumerate(frame_buffer):
            x0 = i % self.width
            y0 = i // self.width
            x = self._pad_x + x0 + 1
            y = self._pad_y + y0 + 1
            if self._in(x, y):
                ch = self._ch(color.ch, mode)
                self._addch(x, y, ch, color.fg, color.bg)

        self._draw_cursor()
        self._refresh()

    def no_cursor(self):
        self._has_cursor = False

    def cursor(self):
        self._has_cursor = True

    def exit(self):
        self._write('\x1b[?25h')

    def move_up(self):
        next_y = self.cursor_y - 1
        next_x = self.cursor_x
        self._update_cursor(next_x, next_y)

    def move_left(self):
        next_y = self.cursor_y
        next_x = self.cursor_x - 1
        self._update_cursor(next_x, next_y)

    def move_right(self):
        next_y = self.cursor_y
        next_x = self.cursor_x + 1
        self._update_cursor(next_x, next_y)

    def move_down(self):
        next_y = self.cursor_y + 1
        next_x = self.cursor_x
        self._update_cursor(next_x, next_y)

    def _draw_cursor(self):
        cx = self._pad_x + 1 + self.cursor_x
        cy = self._pad_y + 1 + self.cursor_y
        self._move(cx, cy)

    def _draw_background(self):
        if self._has_background:
            return

        self._content += '\x1b[0m'

        for i in range(self.window_width):
            for j in range(self.window_height):
                self._addch(i, j, ' ', constants.BLACK, constants.BLACK)

        self._has_background = True
        self._refresh()

    def _ch(self, ch, mode):
        if isinstance(ch, tuple):
            ch_w = ch[1]
            ch = ch[0] + ' '
        else:
            ch_w = get_char_width(ch)

        if mode == constants.DOUBLE and ch_w == 1:
            ch += ch
        return ch

    def _update_cursor(self, x, y):
        if self._in(x, y):
            self.pcursor_x = self.cursor_x
            self.pcursor_y = self.cursor_y
            self.cursor_x = x
            self.cursor_y = y

    def _move(self, x, y):
        if self._in(x, y):
            self._content += f'\x1b[{y + 1};{x + 1};H'

    def _addch(self, x, y, ch, fg=None, bg=None):
        csi_pos = f'\x1b[{y + 1};{x + 1};H'
        if fg != None and bg != None:
            csi_fg = f'\x1b[38;5;{fg}m'
            csi_bg = f'\x1b[48;5;{bg}m'
            content = f'{csi_pos}{csi_fg}{csi_bg}{ch}'
        else:
            content = f'{csi_pos}{ch}'
        self._content += content

    def _clear(self):
        self._write('\x1b[2J')

    def _refresh(self):
        csi_cursor = '\x1b[?25h' if self._has_cursor else '\x1b[?25l'
        self._write(self._content + csi_cursor)
        self._content = ''

    def _draw_border(self):
        self._content += '\x1b[0m'

        for i in range(self._pad_width):
            x = self._pad_x + i
            y = self._pad_y
            if self._in(x, y):
                ch = '+' if i == 0 else '-'
                self._addch(x, y, ch)

        # right
        for i in range(self._pad_height - 1):
            x = self._pad_x + self._pad_width - 1
            y = self._pad_y + i
            if self._in(x, y):
                ch = '+' if i == 0 else '|'
                self._addch(x, y, ch)

        # left
        for i in range(self._pad_height - 1):
            x = self._pad_x
            y = self._pad_y + 1 + i
            if self._in(x, y):
                ch = '+' if i == self._pad_height - 2 else '|'
                self._addch(x, y, ch)

        # bottom
        for i in range(self._pad_width - 1):
            x = self._pad_x + 1 + i
            y = self._pad_y + self._pad_height - 1
            if self._in(x, y):
                ch = '+' if i == self._pad_width - 2 else '-'
                self._addch(x, y, ch)

        self._refresh()

    def _in(self, x, y):
        return x >= 0 and x < self.window_width and y >= 0 and y < self.window_height

    def _resize(self):
        self._update_window_size()
        self._pad_x = (self.window_width - self._pad_width) // 2
        self._pad_y = (self.window_height - self._pad_height) // 2

    def _write(self, content):
        sys.stdout.write(content)
        sys.stdout.flush()


if sys.platform == WINDOWS:
    class WindowsContext(Context):
        def __init__(self):
            pass

        def init(self):
            pass

        def get_window_size(self):
            pass

        def close(self):
            pass

        def get_events(self):
            pass

        def background(self):
            pass

        def _update_window_size(self):
            pass
else:
    import curses

    class CursesContext(Context):

        def __init__(self):
            super(CursesContext, self).__init__()
            self._screen = curses.initscr()
            self.window_width = self._screen.getmaxyx()[1]
            self.window_height = self._screen.getmaxyx()[0]
            curses.endwin()
            self._screen = None

        def init(self):
            self._screen = curses.initscr()
            self._screen.keypad(1)
            self._screen.nodelay(1)
            self._screen.leaveok(False)
            self._key = None
            self._key_pressed_time = None
            self._key_thres = 0.5
            self._window_resized_time = None
            self._window_thres = 2
            self._window_resized = False

            # init
            curses.noecho()
            curses.cbreak()
            curses.start_color()

            # Enable mouse events
            curses.mousemask(
                curses.ALL_MOUSE_EVENTS |
                curses.REPORT_MOUSE_POSITION
            )

        def get_window_size(self):
            if self._screen:
                return self.window_width, self.window_height
            else:
                self._screen = curses.initscr()
                self.window_width = self._screen.getmaxyx()[1]
                self.window_height = self._screen.getmaxyx()[0]
                curses.endwin()
                self._screen = None
                return self.window_width, self.window_height

        def close(self):
            if self._screen:
                self._screen.keypad(0)
            curses.nocbreak()
            curses.echo()
            curses.endwin()

        def get_events(self):
            event_queue = []
            key = self._screen.getch()
            key_pressed = False

            while key != -1:
                if key == curses.KEY_RESIZE:
                    self._resize()
                    self._window_resized = True
                    self._window_resized_time = time.time()
                    event_queue.append(WindowEvent('start'))
                elif key == curses.KEY_MOUSE:
                    _, x, y, _, bstate = curses.getmouse()
                    event_queue += self._get_mouse_events(bstate, x, y)
                else:
                    event_queue.append(KeyboardEvent(key, 'pressed'))
                    event_queue.append(KeyboardEvent(key, 'typed'))
                    key_pressed = True
                    self.key_pressed = True
                    self._key = key
                    self._key_pressed_time = time.time()
                key = self._screen.getch()

            now = time.time()
            if self._window_resized:
                timeout = now - self._window_resized_time > self._window_thres
                if timeout:
                    event_queue.append(WindowEvent('end'))
                    self._window_resized = False

            if self._key_pressed_time != None and not key_pressed:
                timeout = now - self._key_pressed_time > self._key_thres
                if timeout:
                    event_queue.append(KeyboardEvent(self._key, 'released'))
                    self.key_pressed = False
                    self._key = None
                    self._key_pressed_time = None

            return event_queue

        def background(self, color, mode):
            ch = self._ch(color.ch, mode)
            self._content = ""
            for i in range(self.width):
                for j in range(self.height):
                    self._addch(i, j, ch, color.fg, color.bg)
            self._refresh()

        def _update_window_size(self):
            curses.update_lines_cols()
            self.window_width = self._screen.getmaxyx()[1]
            self.window_height = self._screen.getmaxyx()[0]

        def _get_mouse_events(self, bstate, x, y):
            event_queue = []
            x_in = x > self._pad_x and x < self._pad_x + self._pad_width
            y_in = y > self._pad_y and y < self._pad_y + self._pad_height

            if x_in and y_in:
                x = x - (self._pad_x + 1)
                y = y - (self._pad_y + 1)
                is_left_pressed = bstate & curses.BUTTON1_PRESSED != 0
                is_left_clicked = bstate & curses.BUTTON1_CLICKED != 0
                is_left_released = bstate & curses.BUTTON1_RELEASED != 0
                is_right_pressed = bstate & curses.BUTTON3_PRESSED != 0
                is_right_clicked = bstate & curses.BUTTON3_CLICKED != 0
                is_right_released = bstate & curses.BUTTON3_RELEASED != 0

                if is_left_pressed or is_left_clicked:
                    event_queue.append(
                        MouseEvent(x, y, 'pressed', constants.LEFT)
                    )

                if is_left_clicked:
                    event_queue.append(
                        MouseEvent(x, y, 'clicked', constants.LEFT)
                    )

                if is_left_released or is_left_clicked:
                    event_queue.append(
                        MouseEvent(x, y, 'released', constants.LEFT)
                    )

                if is_right_pressed or is_right_clicked:
                    event_queue.append(
                        MouseEvent(x, y, 'pressed', constants.RIGHT)
                    )

                if is_right_clicked:
                    event_queue.append(
                        MouseEvent(x, y, 'clicked', constants.RIGHT)
                    )

                if is_right_released or is_right_clicked:
                    event_queue.append(
                        MouseEvent(x, y, 'released', constants.RIGHT)
                    )
            return event_queue


class LocalTimer(object):

    def run(self, ms, callback):
        while True:
            t1 = time.time()
            stop = callback()
            if not stop:
                t2 = time.time()
                d = ms / 1000 - (t2 - t1)
                if d > 0:
                    time.sleep(d)
            else:
                break

    def stop(self):
        pass

    def wait(self):
        input()


class Shape(object):

    def __init__(
        self,
        points=None,
        is_auto=True,
        primitive_type=constants.POLYGON,
        close_mode=constants.CLOSE,
        options=None
    ):
        self.points = [] if points == None else points
        self.options = {} if options == None else options
        self.is_auto = is_auto
        self.primitive_type = primitive_type
        self.close_mode = close_mode
        self.fill_color = None
        self.stroke_color = None
        self.tint_color = None
        self.stroke_weight = None
        self.transform_matrix_stack = []
        self.is_stroke_enabled = True
        self.is_fill_enabled = True
        self.is_tint_enabled = False

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

    def __init__(
        self,
        x,
        y,
        color=None,
        weight_x=0,
        weight_y=0,
        rotation=0,
        type="normal",
        visible=True
    ):
        self.x = x
        self.y = y
        self.weight_x = weight_x
        self.weight_y = weight_y
        self.type = type
        self.rotation = rotation
        self.visible = visible
        self.color = Color(' ') if color == None else color

    def __str__(self):
        attrs = {
            "x": self.x,
            "y": self.y,
            "color": self.color.ch
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
        return hash(f'({self.x}, {self.y})')

    __repr__ = __str__


class Color(object):

    color_mode = constants.ANSI
    color_channels = (255,)

    def __init__(self, ch=" ", fg=None, bg=None):
        self.ch = ch
        fg, bg = self._preprocess_channels(fg, bg)
        self.fg = self._to_ansi256(fg)
        self.bg = self._to_ansi256(bg)

    def _to_ansi256(self, channels):
        if self.color_mode == constants.ANSI:
            return round(map(channels, 0, self.color_channels[0], 0, 255))
        else:
            c1, c2, c3 = [
                map(c, 0, self.color_channels[i], 0, 1)
                for i, c in enumerate(channels)
            ]
            if self.color_mode == constants.RGB:
                return self.rgb_to_ansi256(c1, c2, c3)
            else:
                return self.hsv_to_ansi256(c1, c2, c3)

    @classmethod
    def _preprocess_channels(cls, fg, bg):
        if cls.color_mode == constants.ANSI:
            fg = cls._preprocess(fg, constants.WHITE)
            bg = cls._preprocess(bg, constants.BLACK)
        elif cls.color_mode == constants.RGB:
            m1, m2, m3 = cls.color_channels  # pylint: disable=unbalanced-tuple-unpacking
            fg = cls._preprocess(fg, (m1, m2, m3))
            bg = cls._preprocess(bg, (0, 0, 0))
        elif cls.color_mode == constants.HSB:
            m1, m2, m3 = cls.color_channels  # pylint: disable=unbalanced-tuple-unpacking
            fg = cls._preprocess(fg, (m1, 0, m3))
            bg = cls._preprocess(bg, (0, 0, 0))
        return fg, bg

    @staticmethod
    def _preprocess(channels, defalut):
        if channels == None:
            return defalut

        if isinstance(channels, tuple) and len(channels) == 1:
            g = channels[0]
            channels = (g, g, g)

        return channels

    def _eq_channels(self, a, b):
        if isinstance(a, tuple) and len(a) == 3:
            v0 = a[0] == b[0]
            v1 = a[1] == b[1]
            v2 = a[2] == b[2]
            return v0 and v1 and v2

        v1 = a if not isinstance(a, tuple) else a[0]
        v2 = b if not isinstance(b, tuple) else b[0]
        return v1 == v2

    def __eq__(self, other):
        if other == None:
            return False
        ch = self._eq_channels(self.ch, other.ch)
        fg = self._eq_channels(self.fg, other.fg)
        bg = self._eq_channels(self.bg, other.bg)
        if ch and self.ch == " ":
            return bg
        else:
            return ch and fg and bg

    def __len__(self):
        return get_char_width(self.ch)

    @classmethod
    def create(cls, ch, fg, bg):
        cls.save()
        cls.color_mode = constants.ANSI
        cls.color_channels = (255,)
        c = cls(ch, fg, bg)
        cls.restore()
        return c

    @classmethod
    def rgb_to_ansi256(cls, r, g, b):
        r *= 255
        g *= 255
        b *= 255
        if r == g and g == b:
            if r < 8:
                return 16
            if r > 248:
                return 231
            return round(((r - 8) / 247) * 24) + 232

        ansi = 16 \
            + (36 * round(r / 255 * 5)) \
            + (6 * round(g / 255 * 5)) \
            + round(b / 255 * 5)

        return ansi

    @classmethod
    def ansi256_to_rgb(cls, v):
        if v < 16:
            return cls.ansi16_to_rgb(v)

        if v >= 232:
            c = (v - 232) * 10 + 8
            return (c, c, c)

        v -= 16
        rem = v % 36
        r = math.floor(v / 36) / 5 * 255
        g = math.floor(rem / 6) / 5 * 255
        b = (rem % 6) / 5 * 255
        return (r / 255, g / 255, b / 255)

    @classmethod
    def ansi16_to_rgb(cls, v):
        color = v % 10
        if color == 0 or color == 7:
            if v > 50:
                color += 3.5
            color = color / 10.5 * 255
            return (color / 255, color / 255, color / 255)

        mult = (~~(v > 50) + 1) * 0.5
        r = (color & 1) * mult
        g = ((color >> 1) & 1) * mult
        b = ((color >> 2) & 1) * mult
        return (r, g, b)

    @classmethod
    def rgb_to_hsb(cls, r, g, b):
        return colorsys.rgb_to_hsv(r, g, b)

    @classmethod
    def hsb_to_rgb(cls, h, s, b):
        return colorsys.hsv_to_rgb(h, s, b)

    @classmethod
    def hsv_to_ansi256(cls, h, s, v):
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        return cls.rgb_to_ansi256(r, g, b)

    @classmethod
    def save(cls):
        cls._color_channels = cls.color_channels
        cls._color_mode = cls.color_mode

    @classmethod
    def restore(cls):
        cls.color_channels = cls._color_channels
        cls.color_mode = cls._color_mode

    def __str__(self):
        attrs = {
            "ch": self.ch,
            "fg": self.fg,
            "bg": self.bg
        }
        return attrs.__str__()

    __repr__ = __str__


class Image(object):

    def __init__(self, image, x, y, width, height):
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def to_shape(self):
        Color.save()
        Color.color_mode = constants.RGB
        Color.color_channels = (255, 255, 255)

        points = []
        y1 = self.y
        y2 = self.y + self.height
        x1 = self.x
        x2 = self.x + self.width
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                y0 = int(map(y, y1, y2, 0, self.image.height - 1))
                x0 = int(map(x, x1, x2, 0, self.image.width - 1))
                index = y0 * self.image.width + x0
                color = self.image[index]
                if color[3] == 0:
                    points.append(Point(x, y, visible=False))
                else:
                    v = (color[0], color[1], color[2])
                    c = Color('·', v, v)
                    points.append(Point(x, y, color=c))

        Color.restore()

        options = {
            'width': self.width,
            'height': self.height
        }
        return Shape(points=points, primitive_type=constants.IMAGE, options=options)


class Text(object):

    def __init__(self, text, x, y, mode):
        self.text = text
        self.x = x
        self.y = y
        self.mode = mode
        self._matrix = [[]]

    def to_shape(self, size, font, align_x, align_y):
        self.to_string(size, font, align_x, align_y)
        points = []
        for i, chars in enumerate(self._matrix):
            ch = ''
            x0 = self.x
            y0 = self.y + i
            for j, c in enumerate(chars):
                # compress the line
                if self.mode == constants.DOUBLE:
                    w1 = get_char_width(ch)
                    w2 = get_char_width(c)
                    w = w1 + w2
                    if w < 2:
                        ch += c
                        continue
                    else:
                        ch = ch + c if w == 2 else ch
                        points.append(Point(x0, y0, color=Color(ch)))
                        ch = '' if w == 2 else c
                        x0 = x0 + 1
                else:
                    x0 = self.x + j
                    points.append(Point(x0, y0, color=Color(c)))

            if ch != '':
                points.append(Point(x0, y0, color=Color(ch)))

        return Shape(points=points, primitive_type=constants.TEXT)

    def to_string(self, size, font, align_x, align_y):
        self.text = self._convert(self.text, size, font)
        self._matrix = self._matrixlize(self.text)
        height = self._matrix.row
        width = self._matrix.col

        if align_x == constants.RIGHT:
            self.x -= width
        elif align_x == constants.CENTER:
            self.x -= width / 2

        if align_y == constants.BOTTOM:
            self.y -= height
        elif align_y == constants.MIDDLE:
            self.y -= height / 2

    @classmethod
    def text_width(cls, text, size, font):
        text = cls._convert(text, size, font)
        matrix = cls._matrixlize(text)
        return matrix.col

    @classmethod
    def text_height(cls, text, size, font):
        text = cls._convert(text, size, font)
        matrix = cls._matrixlize(text)
        return matrix.row

    @classmethod
    def _convert(cls, text, size, font):
        if size == constants.BIG:
            f = Figlet(font=font)
            text = f.renderText(text)
        elif size == constants.LARGE:
            f = Figlet(font=font)
            matrix = cls._matrixlize(text)
            max_width_list = [-1 for _ in range(matrix.col)]
            max_height = -1
            total_width = 0
            steps = []

            for j in range(matrix.col):
                for i in range(matrix.row):
                    ftext = f.renderText(matrix[i][j])
                    m = cls._matrixlize(ftext, False)
                    max_width_list[j] = max(max_width_list[j], m.col)
                    max_height = max(max_height, m.row)
                    matrix[i][j] = m
                start = total_width
                end = start + max_width_list[j]
                total_width = end
                steps.append((start, end))

            def get_info(n):
                for i, (start, end) in enumerate(steps):
                    if n >= start and n < end:
                        return [i, start, end]
                return -1

            text = ""
            for i in range(matrix.row * max_height):
                for j in range(total_width):
                    y0 = int(i / max_height)
                    x0, start, _ = get_info(j)
                    y = i % max_height
                    x = j - start

                    width = max_width_list[x0]
                    m = matrix[y0][x0]
                    mx1 = int((width - m.col) / 2)
                    mx2 = mx1 + m.col
                    my1 = int((max_height - m.row) / 2)
                    my2 = my1 + m.row

                    if x < mx1 or x >= mx2 or y < my1 or y >= my2:
                        text += " "
                    else:
                        text += m[y - my1][x - mx1]
                text += "\n"
        return text

    @staticmethod
    def _matrixlize(text, no_empty_line=True):
        if no_empty_line:
            lines = [
                line for line in text.split('\n')
                if not line in string.whitespace or len(line) == 1
            ]
        else:
            lines = [line for line in text.split('\n')]

        if len(lines) == 0:
            return Matrix([[]])

        max_width = max([len(line) for line in lines])
        matrix = [
            [line[i] if i < len(line) else ' '
             for i in range(max_width)]
            for line in lines
        ]
        return Matrix(matrix)


class Event(object):
    type = ""

    def __init__(self, type):
        self.type = type


class WindowEvent(Event):
    def __init__(self, event_type):
        super(WindowEvent, self).__init__('window')
        self.event_type = event_type


class MouseEvent(Event):
    mouse_type = ""

    def __init__(self, x, y, event_type, button_type):
        super(MouseEvent, self).__init__('mouse')
        self.x = x
        self.y = y
        self.event_type = event_type
        self.button_type = button_type


class KeyboardEvent(Event):

    _KEY_MAP = {
        9: constants.TAB,
        10: constants.ENTER,
        27: constants.ESCAPE,
        32: constants.SPACE,
        127: constants.BACKSPACE,
        260: constants.LEFT,
        259: constants.UP,
        261: constants.RIGHT,
        258: constants.DOWN
    }

    def __init__(self, key, event_type):
        super(KeyboardEvent, self).__init__('keyboard')
        self.event_type = event_type
        if key in self._KEY_MAP:
            self.key_code = self._KEY_MAP[key]
            self.key = constants.CODED
        else:
            self.key_code = None
            char = chr(key)
            if char == "":
                self.key = key
            else:
                self.key = char
