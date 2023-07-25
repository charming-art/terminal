extern crate wasm_bindgen;
use crate::{
    matrix3::{matrix3_rotate, matrix3_scale, matrix3_transform, matrix3_translate},
    renderer::Renderer,
};
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
impl Renderer {
    pub fn translate(&mut self, x: f64, y: f64) {
        self.mode_view = matrix3_translate(&self.mode_view, x, y);
    }

    pub fn scale(&mut self, x: f64, y: f64) {
        self.mode_view = matrix3_scale(&self.mode_view, x, y);
    }

    pub fn rotate(&mut self, rad: f64) {
        self.mode_view = matrix3_rotate(&self.mode_view, rad);
    }

    #[wasm_bindgen(js_name = "pushMatrix")]
    pub fn push_matrix(&mut self) {
        self.stacks.push(self.mode_view);
    }

    #[wasm_bindgen(js_name = "popMatrix")]
    pub fn pop_matrix(&mut self) {
        if let Some(last) = self.stacks.pop() {
            self.mode_view = last;
        }
    }

    pub fn transform(&mut self, x: f64, y: f64) -> *const f64 {
        self.out = matrix3_transform(&[x, y, 1.0], &self.mode_view);
        self.out.as_ptr()
    }
}
