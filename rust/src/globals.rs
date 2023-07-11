pub const CELL_SIZE: usize = 4;

pub const NULL_VALUE: u32 = 0xFFFFFFFF;

pub struct Vertex {
    pub(crate) color: Color,
    pub(crate) x: isize,
    pub(crate) y: isize,
}

#[derive(Clone, Copy)]
pub struct Color(
    pub(crate) u32,
    pub(crate) u32,
    pub(crate) u32,
    pub(crate) u32,
);

pub struct Shape {
    pub(crate) vertices: Vec<Vertex>,
}
