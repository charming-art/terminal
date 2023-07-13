extern crate wasm_bindgen;
use crate::{globals::Color, renderer::Renderer};
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
impl Renderer {
    pub fn stroke(&mut self, ch: u32, ch1: u32, fg: u32, bg: u32) {
        self.stroke_color = Color(ch, ch1, fg, bg);
    }
}

#[cfg(test)]
mod tests {
    use super::Renderer;

    #[test]
    fn should_set_stroke() {
        let mut renderer: Renderer = Renderer::new(10, 10);
        renderer.stroke(0, 0, 0, 0);
        assert_eq!(renderer.stroke_color.0, 0);
        assert_eq!(renderer.stroke_color.1, 0);
        assert_eq!(renderer.stroke_color.2, 0);
        assert_eq!(renderer.stroke_color.3, 0);
    }
}
