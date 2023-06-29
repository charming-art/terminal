extern crate wasm_bindgen;

use std::vec;

use wasm_bindgen::prelude::*;

const CELL_SIZE: usize = 3;

struct Vertex {
    color: Color,
    x: isize,
    y: isize,
}

#[derive(Clone, Copy)]
struct Color(i32, i32, i32);

struct Shape {
    vertices: Vec<Vertex>,
}

#[wasm_bindgen]
pub struct Rasterizer {
    cols: usize,
    rows: usize,
    stroke: Color,
    buffer: Vec<i32>,
    shapes: Vec<Shape>,
}

#[wasm_bindgen]
impl Rasterizer {
    pub fn new(cols: usize, rows: usize) -> Rasterizer {
        let buffer: Vec<i32> = vec![-1; cols * rows * CELL_SIZE];
        Rasterizer {
            cols,
            rows,
            buffer,
            stroke: Color(0, 0, 0),
            shapes: vec![],
        }
    }
    pub fn stroke(&mut self, ch: i32, fg: i32, bg: i32) {
        self.stroke = Color(ch, fg, bg);
    }
    pub fn point(&mut self, x: isize, y: isize) {
        let vertices: Vec<Vertex> = vec![Vertex {
            color: self.stroke,
            x: x,
            y: y,
        }];
        let point: Shape = Shape { vertices };
        self.shapes.push(point);
    }
    pub fn render(&mut self) -> *const i32 {
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
                }
            }
        }
        self.buffer.as_ptr()
    }
}
