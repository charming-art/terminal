extern crate wasm_bindgen;
use crate::{
    globals::{Shape, Vertex},
    renderer::Renderer,
};
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
impl Renderer {
    pub fn point(&mut self, x: f64, y: f64) {
        let vertices: Vec<Vertex> = vec![Vertex {
            color: self.stroke_color,
            x: x,
            y: y,
        }];
        let point: Shape = Shape {
            vertices,
            matrix: self.mode_view,
        };
        self.shapes.push(point);
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
