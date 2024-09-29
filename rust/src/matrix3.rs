use crate::globals::{Matrix3, Vector3};

pub fn matrix3_identity() -> Matrix3 {
    [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
}

pub fn matrix3_zero() -> Matrix3 {
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
}

// x'   a b c   x
// y' = d e f * y
// z'   g h i   z
pub fn matrix3_transform(v: &Vector3, m: &Matrix3) -> Vector3 {
    let mut out: Vector3 = [0.0, 0.0, 0.0];
    let x: f64 = v[0];
    let y: f64 = v[1];
    let z: f64 = v[2];
    out[0] = x * m[0] + y * m[1] + z * m[2];
    out[1] = x * m[3] + y * m[4] + z * m[5];
    out[2] = x * m[6] + y * m[7] + z * m[8];
    out
}

// x'   a b c   1 0 x   x
// y' = d e f * 0 1 y * y
// 1    g h i   0 0 1   1
pub fn matrix3_translate(a: &Matrix3, x: f64, y: f64) -> Matrix3 {
    let mut out: Matrix3 = matrix3_zero();
    out[0] = a[0];
    out[1] = a[1];
    out[2] = a[0] * x + a[1] * y + a[2];
    out[3] = a[3];
    out[4] = a[4];
    out[5] = a[3] * x + a[4] * y + a[5];
    out[6] = a[6];
    out[7] = a[7];
    out[8] = a[6] * x + a[7] * y + a[8];
    out
}

// x'   a b c   x 0 0   x0
// y' = d e f * 0 y 0 * y0
// 1    g h i   0 0 1   1
pub fn matrix3_scale(a: &Matrix3, x: f64, y: f64) -> Matrix3 {
    let mut out: Matrix3 = matrix3_zero();
    out[0] = x * a[0];
    out[1] = y * a[1];
    out[2] = a[2];
    out[3] = x * a[3];
    out[4] = y * a[4];
    out[5] = a[5];
    out[6] = x * a[6];
    out[7] = y * a[7];
    out[8] = a[8];
    out
}

// x'  a b c   cosx -sinx 0   x
// y'= d e f * sinx cosx  0 * y
// 1   g h i   0    0     1   1
pub fn matrix3_rotate(a: &Matrix3, rad: f64) -> Matrix3 {
    let mut out: Matrix3 = matrix3_zero();
    let cos: f64 = rad.cos();
    let sin: f64 = rad.sin();
    out[0] = a[0] * cos + a[1] * sin;
    out[1] = -a[0] * sin + a[1] * cos;
    out[2] = a[2];
    out[3] = a[3] * cos + a[4] * sin;
    out[4] = -a[3] * sin + a[4] * cos;
    out[5] = a[5];
    out[6] = a[6] * cos + a[7] * sin;
    out[7] = -a[6] * sin + a[7] * cos;
    out[8] = a[8];
    out
}
