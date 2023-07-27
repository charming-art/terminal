extern crate wasm_bindgen;
use crate::{
    globals::{Shape, Vertex},
    renderer::Renderer,
};
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
impl Renderer {
    pub fn point(&mut self, x: f64, y: f64) {
        let v: Vertex = Vertex {
            color: self.stroke_color,
            x,
            y,
        };
        self.shapes.push(Shape {
            vertices: vec![v],
            matrix: self.mode_view,
        });
    }
    pub fn line(&mut self, x: f64, y: f64, x1: f64, y1: f64) {
        let v: Vertex = Vertex {
            color: self.stroke_color,
            x,
            y,
        };
        let v1: Vertex = Vertex {
            color: self.stroke_color,
            x: x1,
            y: y1,
        };
        self.shapes.push(Shape {
            vertices: vec![v, v1],
            matrix: self.mode_view,
        })
    }
}

#[cfg(test)]
mod tests {

    use super::Renderer;

    #[test]
    fn should_add_point() {
        let mut renderer: Renderer = Renderer::new(10, 10);
        renderer.point(0.0, 0.0);
        assert_eq!(renderer.shapes[0].vertices[0].x, 0.0);
        assert_eq!(renderer.shapes[0].vertices[0].y, 0.0);
    }
}
