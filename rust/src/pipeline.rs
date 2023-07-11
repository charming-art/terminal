extern crate wasm_bindgen;
use crate::{globals::CELL_SIZE, globals::NULL_VALUE, renderer::Renderer};
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
impl Renderer {
    pub fn render(&mut self) -> *const u32 {
        self.buffer.fill(NULL_VALUE);
        for shape in &self.shapes {
            for vertex in &shape.vertices {
                let x: isize = vertex.x;
                let y: isize = vertex.y;
                let cols: isize = self.cols as isize;
                let rows: isize = self.rows as isize;
                if x >= 0 && x < cols && y >= 0 && y < rows {
                    let index: usize = ((x + y * cols) as usize) * CELL_SIZE;
                    self.buffer[index] = vertex.color.0;
                    self.buffer[index + 1] = vertex.color.1;
                    self.buffer[index + 2] = vertex.color.2;
                    self.buffer[index + 3] = vertex.color.3;
                }
            }
        }
        self.shapes.clear();
        self.buffer.as_ptr()
    }
}

#[cfg(test)]
mod tests {
    use super::Renderer;

    #[test]
    fn should_clear_shapes() {
        let mut renderer: Renderer = Renderer::new(10, 10);
        renderer.point(0, 0);
        renderer.render();
        assert_eq!(renderer.shapes.len(), 0);
    }
}
