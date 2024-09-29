extern crate wasm_bindgen;
use crate::{
    globals::{Color, Matrix3, Shape, Vector3, CELL_SIZE, NULL_VALUE},
    matrix3::matrix3_identity,
};
use std::vec;
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub struct Renderer {
    pub(crate) cols: usize,
    pub(crate) rows: usize,
    pub(crate) stroke_color: Color,
    pub(crate) fill_color: Color,
    pub(crate) has_stroke: bool,
    pub(crate) has_fill: bool,
    pub(crate) has_background: bool,
    pub(crate) background_color: Color,
    pub(crate) buffer: Vec<u32>,
    pub(crate) shapes: Vec<Shape>,
    pub(crate) mode_view: Matrix3,
    pub(crate) out: Vector3,
    pub(crate) stacks: Vec<Matrix3>,
}

#[wasm_bindgen]
impl Renderer {
    pub fn new(cols: usize, rows: usize) -> Renderer {
        let buffer: Vec<u32> = vec![NULL_VALUE; cols * rows * CELL_SIZE];
        Renderer {
            cols,
            rows,
            buffer,
            stroke_color: [NULL_VALUE, NULL_VALUE, NULL_VALUE, NULL_VALUE],
            fill_color: [NULL_VALUE, NULL_VALUE, NULL_VALUE, NULL_VALUE],
            has_fill: false,
            has_stroke: true,
            has_background: false,
            background_color: [NULL_VALUE, NULL_VALUE, NULL_VALUE, NULL_VALUE],
            mode_view: matrix3_identity(),
            stacks: vec![],
            shapes: vec![],
            out: [0.0, 0.0, 0.0],
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
        assert_eq!(renderer.stacks.len(), 0);
        assert_eq!(renderer.has_stroke, true);
        assert_eq!(renderer.has_background, false);
        assert_eq!(renderer.has_fill, false);
    }
}
