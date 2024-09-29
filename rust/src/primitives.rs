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
            is_closed: false,
            has_fill: false,
            has_stroke: self.has_stroke,
            fill_color: self.fill_color,
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
            is_closed: false,
            has_fill: false,
            has_stroke: self.has_stroke,
            fill_color: self.fill_color,
        })
    }
    pub fn rect(&mut self, x: f64, y: f64, width: f64, height: f64) {
        if width == 0.0 || height == 0.0 {
            return;
        }
        let dx: f64 = width - 1.0;
        let dy: f64 = height - 1.0;
        let v: Vertex = Vertex {
            color: self.stroke_color,
            x,
            y,
        };
        let v1: Vertex = Vertex {
            color: self.stroke_color,
            x: x + dx,
            y,
        };
        let v2: Vertex = Vertex {
            color: self.stroke_color,
            x: x + dx,
            y: y + dy,
        };
        let v3: Vertex = Vertex {
            color: self.stroke_color,
            x,
            y: y + dy,
        };
        self.shapes.push(Shape {
            vertices: vec![v, v1, v2, v3],
            matrix: self.mode_view,
            is_closed: true,
            has_fill: self.has_fill,
            has_stroke: self.has_stroke,
            fill_color: self.fill_color,
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
