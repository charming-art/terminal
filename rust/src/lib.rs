extern crate wasm_bindgen;

use std::vec;

use wasm_bindgen::prelude::*;

const CELL_SIZE: usize = 4;

const NULL_VALUE: u32 = 0xFFFFFFFF;

struct Vertex {
    color: Color,
    x: isize,
    y: isize,
}

#[derive(Clone, Copy)]
struct Color(u32, u32, u32, u32);

struct Shape {
    vertices: Vec<Vertex>,
}

#[wasm_bindgen]
pub struct Rasterizer {
    cols: usize,
    rows: usize,
    stroke: Color,
    buffer: Vec<u32>,
    shapes: Vec<Shape>,
}

#[wasm_bindgen]
impl Rasterizer {
    pub fn new(cols: usize, rows: usize) -> Rasterizer {
        let buffer: Vec<u32> = vec![NULL_VALUE; cols * rows * CELL_SIZE];
        Rasterizer {
            cols,
            rows,
            buffer,
            stroke: Color(NULL_VALUE, NULL_VALUE, NULL_VALUE, NULL_VALUE),
            shapes: vec![],
        }
    }
    pub fn stroke(&mut self, ch: u32, ch1: u32, fg: u32, bg: u32) {
        self.stroke = Color(ch, ch1, fg, bg);
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
