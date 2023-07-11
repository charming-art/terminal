extern crate wasm_bindgen;
use crate::{globals::Color, globals::Shape, globals::CELL_SIZE, globals::NULL_VALUE};
use std::vec;
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub struct Renderer {
    pub(crate) cols: usize,
    pub(crate) rows: usize,
    pub(crate) stroke_color: Color,
    pub(crate) buffer: Vec<u32>,
    pub(crate) shapes: Vec<Shape>,
}

#[wasm_bindgen]
impl Renderer {
    pub fn new(cols: usize, rows: usize) -> Renderer {
        let buffer: Vec<u32> = vec![NULL_VALUE; cols * rows * CELL_SIZE];
        Renderer {
            cols,
            rows,
            buffer,
            stroke_color: Color(NULL_VALUE, NULL_VALUE, NULL_VALUE, NULL_VALUE),
            shapes: vec![],
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Renderer;

    #[test]
    fn should_have_expected_defaults() {
        let renderer: Renderer = Renderer::new(10, 10);
        assert_eq!(renderer.cols, 10);
        assert_eq!(renderer.rows, 10);
        assert_eq!(renderer.buffer.len(), 400);
        assert_eq!(renderer.shapes.len(), 0);
    }
}
