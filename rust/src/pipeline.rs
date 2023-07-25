extern crate wasm_bindgen;
use crate::{
    globals::{Matrix3, Vector3, Vertex, CELL_SIZE, NULL_VALUE},
    matrix3::{matrix3_identity, matrix3_transform},
    renderer::Renderer,
};
use wasm_bindgen::prelude::*;

fn vertex_processing(vertices: &Vec<Vertex>, m: &Matrix3) -> Vec<Vertex> {
    let mut transformed_vertices: Vec<Vertex> = vec![];
    for vertex in vertices {
        let v: Vector3 = [vertex.x, vertex.y, 1.0];
        let out: Vector3 = matrix3_transform(&v, &m);
        transformed_vertices.push(Vertex {
            color: vertex.color,
            x: out[0],
            y: out[1],
        })
    }
    transformed_vertices
}

#[wasm_bindgen]
impl Renderer {
    pub fn render(&mut self) -> *const u32 {
        self.buffer.fill(NULL_VALUE);
        for shape in &self.shapes {
            let transformed_vertices: Vec<Vertex> =
                vertex_processing(&shape.vertices, &shape.matrix);
            for vertex in transformed_vertices {
                let x: isize = vertex.x.round() as isize;
                let y: isize = vertex.y.round() as isize;
                let cols: isize = self.cols as isize;
                let rows: isize = self.rows as isize;
                if x >= 0 && x < cols && y >= 0 && y < rows {
                    let index: usize = ((x + y * cols) as usize) * CELL_SIZE;
                    self.buffer[index] = vertex.color[0];
                    self.buffer[index + 1] = vertex.color[1];
                    self.buffer[index + 2] = vertex.color[2];
                    self.buffer[index + 3] = vertex.color[3];
                }
            }
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
