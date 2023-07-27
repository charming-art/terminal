pub fn ascending(a: &mut f64, b: &mut f64) {
    if a > b {
        swap(a, b);
    }
}

pub fn swap(a: &mut f64, b: &mut f64) {
    let t: f64 = *a;
    *a = *b;
    *b = t;
}

pub fn map(x: f64, d0: f64, d1: f64, r0: f64, r1: f64) -> f64 {
    let t: f64 = (x - d0) / (d1 - d0);
    r0 * (1.0 - t) + t * r1
}

#[cfg(test)]
mod tests {
    use super::{ascending, map, swap};

    #[test]
    fn should_swap() {
        let mut a: f64 = 2.0;
        let mut b: f64 = 1.0;
        swap(&mut a, &mut b);
        assert_eq!(a, 1.0);
        assert_eq!(b, 2.0);
    }

    #[test]
    fn should_ascending() {
        let mut a: f64 = 2.0;
        let mut b: f64 = 1.0;
        ascending(&mut a, &mut b);
        assert_eq!(a, 1.0);
        assert_eq!(b, 2.0);
    }

    #[test]
    fn should_map() {
        assert_eq!(map(0.4, 0.0, 1.0, 0.0, 10.0), 4.0);
    }
}
