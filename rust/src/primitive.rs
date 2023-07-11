extern crate wasm_bindgen;
use crate::{globals::Shape, globals::Vertex, renderer::Renderer};
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
impl Renderer {
    pub fn point(&mut self, x: isize, y: isize) {
        let vertices: Vec<Vertex> = vec![Vertex {
            color: self.stroke_color,
            x: x,
            y: y,
        }];
        let point: Shape = Shape { vertices };
        self.shapes.push(point);
    }
}
