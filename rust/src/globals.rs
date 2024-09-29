pub const CELL_SIZE: usize = 4;

pub const NULL_VALUE: u32 = 0xFFFFFFFF;

pub struct Vertex {
    pub(crate) color: Color,
    pub(crate) x: f64,
    pub(crate) y: f64,
}

pub struct Point {
    pub(crate) color: Color,
    pub(crate) x: isize,
    pub(crate) y: isize,
}

pub type Edge<'a> = [&'a Point; 2];

pub type Color = [u32; CELL_SIZE];

pub struct Shape {
    pub(crate) vertices: Vec<Vertex>,
    pub(crate) matrix: Matrix3,
    pub(crate) is_closed: bool,
    pub(crate) has_stroke: bool,
    pub(crate) has_fill: bool,
    pub(crate) fill_color: Color,
}

pub type Matrix3 = [f64; 9];

pub type Vector3 = [f64; 3];
