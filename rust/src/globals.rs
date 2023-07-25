pub const CELL_SIZE: usize = 4;

pub const NULL_VALUE: u32 = 0xFFFFFFFF;

pub struct Vertex {
    pub(crate) color: Color,
    pub(crate) x: f64,
    pub(crate) y: f64,
}

pub type Edge<'a> = [&'a Vertex; 2];

pub type Color = [u32; CELL_SIZE];

pub struct Shape {
    pub(crate) vertices: Vec<Vertex>,
    pub(crate) matrix: Matrix3,
}

pub type Matrix3 = [f64; 9];

pub type Vector3 = [f64; 3];
