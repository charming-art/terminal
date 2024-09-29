extern crate wasm_bindgen;
use crate::{
    globals::{Color, Edge, Matrix3, Point, Vector3, Vertex, CELL_SIZE, NULL_VALUE},
    matrix3::{matrix3_identity, matrix3_transform},
    renderer::Renderer,
};
use std::{cmp, ptr};
use wasm_bindgen::prelude::*;

fn vertex_processing(vertices: &Vec<Vertex>, m: &Matrix3) -> Vec<Point> {
    let mut transformed: Vec<Point> = vec![];
    for vertex in vertices {
        let v: Vector3 = [vertex.x, vertex.y, 1.0];
        let out: Vector3 = matrix3_transform(&v, &m);
        transformed.push(Point {
            color: vertex.color,
            x: out[0].round() as isize,
            y: out[1].round() as isize,
        })
    }
    transformed
}

fn primitive_assembly(vertices: &Vec<Point>, is_closed: bool) -> Vec<Edge> {
    if vertices.len() == 0 {
        vec![]
    } else if vertices.len() == 1 {
        let edge: Edge = [&vertices[0], &vertices[0]];
        vec![edge]
    } else {
        let mut edges: Vec<Edge> = vec![];
        let len: usize = vertices.len();
        let end: usize = if is_closed { len + 1 } else { len };
        for i in 1..end {
            let from: &Point = &vertices[i - 1];
            let to: &Point = &vertices[i % len];
            let edge: Edge = [from, to];
            edges.push(edge);
        }
        edges
    }
}

fn rasterization(
    edges: &Vec<Edge>,
    fill_color: Color,
    has_stroke: bool,
    has_fill: bool,
) -> Vec<Point> {
    let mut vertices: Vec<Point> = vec![];
    if has_fill {
        rasterization_stroke(&mut vertices, edges, fill_color, true);
        rasterization_fill(&mut vertices, fill_color);
    }
    if has_stroke {
        rasterization_stroke(&mut vertices, edges, fill_color, false);
    }
    vertices
}

fn rasterization_stroke(
    vertices: &mut Vec<Point>,
    edges: &Vec<Edge>,
    fill_color: Color,
    use_fill: bool,
) {
    for i in 0..edges.len() {
        let edge: Edge = edges[i];
        let from: &Point = edge[0];
        let to: &Point = edge[1];
        if ptr::eq(from, to) {
            vertices.push(Point {
                color: from.color,
                x: from.x,
                y: from.y,
            })
        } else {
            let next: Edge = edges[(i + 1) % edges.len()];
            let next_from: &Point = next[0];
            let color: Color = if use_fill { fill_color } else { from.color };
            let line: &mut Vec<Point> = &mut rasterization_line(from, to, color);
            if next_from.x == to.x && next_from.y == to.y && line.len() >= 2 {
                line.pop();
                vertices.append(line);
            } else {
                vertices.append(line);
            }
        }
    }
}

fn rasterization_fill(vertices: &mut Vec<Point>, color: Color) {
    let mut y0: isize = isize::MAX;
    let mut y1: isize = isize::MIN;
    for vertex in &mut *vertices {
        y0 = cmp::min(y0, vertex.y);
        y1 = cmp::max(y1, vertex.y);
    }

    let mut lookup: Vec<Vec<isize>> = vec![vec![]; (y1 - y0) as usize + 1];
    for vertex in &mut *vertices {
        let index: usize = (vertex.y - y0) as usize;
        lookup[index].push(vertex.x as isize)
    }

    for i in 0..lookup.len() {
        let line: &mut Vec<isize> = &mut lookup[i];
        line.sort();
        let y: isize = (i as isize) + y0;
        let mut in_polygon: bool = false;
        for i in 0..line.len() {
            if in_polygon {
                let x0: isize = line[i - 1];
                let x1: isize = line[i];
                for x in (x0 + 1)..x1 {
                    vertices.push(Point { color, x, y })
                }
            }
            in_polygon = !in_polygon;
        }
    }
}

// @see https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
fn rasterization_line(from: &Point, to: &Point, color: Color) -> Vec<Point> {
    let dx: isize = (to.x - from.x).abs();
    let dy: isize = -(to.y - from.y).abs();
    let sx: isize = if from.x < to.x { 1 } else { -1 };
    let sy: isize = if from.y < to.y { 1 } else { -1 };
    let mut vertices: Vec<Point> = vec![];
    let mut x: isize = from.x;
    let mut y: isize = from.y;
    let mut error: isize = dx + dy;

    loop {
        vertices.push(Point { color, x, y });
        if x == to.x && y == to.y {
            break;
        };
        let error2: isize = error * 2;
        if error2 >= dy {
            if x == to.x {
                break;
            }
            error = error + dy;
            x = x + sx;
        }
        if error2 <= dx {
            if y == to.y {
                break;
            }
            error = error + dx;
            y = y + sy;
        }
    }

    vertices
}

fn clipping(vertices: &Vec<Point>, cols: isize, rows: isize) -> Vec<usize> {
    let mut clipped: Vec<usize> = vec![];
    for i in 0..vertices.len() {
        let vertex: &Point = &vertices[i];
        let x: isize = vertex.x;
        let y: isize = vertex.y;
        if x >= 0 && x < cols && y >= 0 && y < rows {
            clipped.push(i);
        }
    }
    clipped
}

fn fragment_processing(
    vertices: &Vec<Point>,
    clipped: &Vec<usize>,
    buffer: &mut Vec<u32>,
    cols: isize,
) {
    for i in clipped {
        let vertex: &Point = &vertices[*i];
        let x: isize = vertex.x;
        let y: isize = vertex.y;
        let index: usize = ((x + y * cols) as usize) * CELL_SIZE;
        buffer[index] = vertex.color[0];
        buffer[index + 1] = vertex.color[1];
        buffer[index + 2] = vertex.color[2];
        buffer[index + 3] = vertex.color[3];
    }
}

fn background_processing(
    has_background: bool,
    color: Color,
    buffer: &mut Vec<u32>,
    rows: isize,
    cols: isize,
) {
    if has_background {
        for x in 0..cols {
            for y in 0..rows {
                let index: usize = ((x + y * cols) as usize) * CELL_SIZE;
                buffer[index] = color[0];
                buffer[index + 1] = color[1];
                buffer[index + 2] = color[2];
                buffer[index + 3] = color[3];
            }
        }
    } else {
        buffer.fill(NULL_VALUE);
    }
}

#[wasm_bindgen]
impl Renderer {
    pub fn render(&mut self) -> *const u32 {
        background_processing(
            self.has_background,
            self.background_color,
            &mut self.buffer,
            self.rows as isize,
            self.cols as isize,
        );
        for shape in &self.shapes {
            let transformed: Vec<Point> = vertex_processing(&shape.vertices, &shape.matrix);
            let primitive: Vec<Edge> = primitive_assembly(&transformed, shape.is_closed);
            let fragment: Vec<Point> = rasterization(
                &primitive,
                shape.fill_color,
                shape.has_stroke,
                shape.has_fill,
            );
            let clipped: Vec<usize> = clipping(&fragment, self.cols as isize, self.rows as isize);
            fragment_processing(&fragment, &clipped, &mut self.buffer, self.cols as isize);
        }
        self.has_background = false;
        self.has_stroke = true;
        self.has_fill = false;
        self.shapes.clear();
        self.stacks.clear();
        self.mode_view = matrix3_identity();
        self.buffer.as_ptr()
    }
}

#[cfg(test)]
mod tests {
    use super::Renderer;

    #[test]
    fn should_clear_reset() {
        let mut renderer: Renderer = Renderer::new(10, 10);
        renderer.point(0.0, 0.0);
        renderer.render();
        assert_eq!(renderer.shapes.len(), 0);
        assert_eq!(renderer.stacks.len(), 0);
        assert_eq!(renderer.mode_view[0], 1.0);
        assert_eq!(renderer.mode_view[4], 1.0);
        assert_eq!(renderer.mode_view[8], 1.0);
        assert_eq!(renderer.has_background, false);
        assert_eq!(renderer.has_stroke, true);
        assert_eq!(renderer.has_fill, false);
    }
}
