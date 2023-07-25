extern crate wasm_bindgen;
use crate::{
    globals::{Edge, Matrix3, Vector3, Vertex, CELL_SIZE, NULL_VALUE},
    matrix3::{matrix3_identity, matrix3_transform},
    renderer::Renderer,
};
use std::ptr;
use wasm_bindgen::prelude::*;

fn vertex_processing(vertices: &Vec<Vertex>, m: &Matrix3) -> Vec<Vertex> {
    let mut transformed: Vec<Vertex> = vec![];
    for vertex in vertices {
        let v: Vector3 = [vertex.x, vertex.y, 1.0];
        let out: Vector3 = matrix3_transform(&v, &m);
        transformed.push(Vertex {
            color: vertex.color,
            x: out[0],
            y: out[1],
        })
    }
    transformed
}

fn primitive_assembly(vertices: &Vec<Vertex>) -> Vec<Edge> {
    if vertices.len() == 0 {
        vec![]
    } else if vertices.len() == 1 {
        let edge: Edge = [&vertices[0], &vertices[0]];
        vec![edge]
    } else {
        let mut edges: Vec<Edge> = vec![];
        for i in 1..vertices.len() {
            let from: &Vertex = &vertices[i - 1];
            let to: &Vertex = &vertices[i];
            let edge: Edge = [from, to];
            edges.push(edge);
        }
        edges
    }
}

fn rasterization(edges: &Vec<Edge>) -> Vec<Vertex> {
    let mut vertices: Vec<Vertex> = vec![];
    for edge in edges {
        let from: &Vertex = edge[0];
        let to: &Vertex = edge[1];
        if ptr::eq(from, to) {
            vertices.push(Vertex {
                color: from.color,
                x: from.x,
                y: from.y,
            })
        }
    }
    vertices
}

fn clipping(vertices: &Vec<Vertex>, cols: isize, rows: isize) -> Vec<usize> {
    let mut clipped: Vec<usize> = vec![];
    for i in 0..vertices.len() {
        let vertex: &Vertex = &vertices[i];
        let x: isize = vertex.x.round() as isize;
        let y: isize = vertex.y.round() as isize;
        if x >= 0 && x < cols && y >= 0 && y < rows {
            clipped.push(i);
        }
    }
    clipped
}

fn fragment_processing(
    clipped: &Vec<usize>,
    vertices: &Vec<Vertex>,
    buffer: &mut Vec<u32>,
    cols: isize,
) {
    for i in clipped {
        let vertex: &Vertex = &vertices[*i];
        let x: isize = vertex.x.round() as isize;
        let y: isize = vertex.y.round() as isize;
        let index: usize = ((x + y * cols) as usize) * CELL_SIZE;
        buffer[index] = vertex.color[0];
        buffer[index + 1] = vertex.color[1];
        buffer[index + 2] = vertex.color[2];
        buffer[index + 3] = vertex.color[3];
    }
}

#[wasm_bindgen]
impl Renderer {
    pub fn render(&mut self) -> *const u32 {
        self.buffer.fill(NULL_VALUE);
        for shape in &self.shapes {
            let transformed: Vec<Vertex> = vertex_processing(&shape.vertices, &shape.matrix);
            let primitive: Vec<Edge> = primitive_assembly(&transformed);
            let fragment: Vec<Vertex> = rasterization(&primitive);
            let clipped: Vec<usize> = clipping(&fragment, self.cols as isize, self.rows as isize);
            fragment_processing(&clipped, &fragment, &mut self.buffer, self.cols as isize);
        }
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
    }
}
