extern crate wasm_bindgen;
use crate::{globals::Color, renderer::Renderer};
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
impl Renderer {
    pub fn stroke(&mut self, ch: u32, ch1: u32, fg: u32, bg: u32) {
        self.stroke_color = Color(ch, ch1, fg, bg);
    }
}
