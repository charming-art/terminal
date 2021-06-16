# Math

Methods related to math.

## CVector

Methods for manipulation vector object which is useful for simulating physic system.

<a name="cvector" href="#cvector">#</a> cm.**CVector**(*x*=0, *y*=0) : *CVector*

A class to describe a two dimensional vector, specifically a Euclidean (also known as geometric) vector.

```py
from charming import CVector

v1 = CVector() 
v2 = CVector(1, 2)

v1 # (0, 0)
v2 # (1, 2)
```

<a name="set" href="#set">#</a> cvector.**set**(*x*=0", *y*=0) : *CVector* <br/>
<a name="set" href="#set">#</a> cvector.**set**(*vector*) : *CVector* <br/>
<a name="set" href="#set">#</a> cvector.**set**(*list*) : *CVector* <br/>

Set the components of the vector.

```py
from charming import CVector

v = CVector()
v.set(1, 2) # (1, 2)

v1 = CVector()
v1.set(v) # (1, 2)
v1.set([2, 3]) # (2, 3)
```

<a name="random_2D" href="#random_2D">#</a> CVector.**random_2D**() : *CVector*

Make a new 2D unit vector with a random direction.

```py
from charming import CVector
from math import isclose

v = CVector.random_2D()
isclose(v.mag, 1.0) # true
```

<a name="from_angle" href="#from_angle">#</a> CVector.**from_angle**() : *CVector*

Make a new 2D unit vector from an angle.

```py
from charming import CVector
from math import pi, isclose

v = CVector.from_angle(math.pi / 3)
isclose(v.mag, 1.0) # true
```

<a name="copy" href="#copy">#</a> cvector.**copy**() : *CVector*

Get a copy of the vector.

```py
from charming import CVector

v = CVector(1, 2)
v1 = v.copy() # (1, 2)
```

<a name="mag" href="#mag">#</a> cvector.**mag**() : *number*

Calculate the magnitude of the vector.

```py
from charming import CVector

v = CVector(3, 4)
v.mag # 5.0
```

<a name="mag_sq" href="#mag_sq">#</a> cvector.**mag_sq**() : *number*

Calculate the magnitude of the vector, squared.

```py
from charming import CVector

v = CVector(3, 4)
v.mag_sq() # 25
```

<a name="add" href="#add">#</a> cvector *+* other : *CVector*

Adds x and y components to a vector, one vector to another, or two independent vectors.

```py
import charming as cm

v1 = cm.CVector(1, 2)
v2 = cm.CVector(3, 4)
v1 + v2 # (4, 6)
v1 += v2 # (4, 6)
```

<a name="sub" href="#sub">#</a> cvector *-* other : *CVector*

Subtract x and y components from a vector, one vector from another, or two independent vectors.

```py
from charming import CVector

v1 = CVector(4, 2)
v2 = CVector(2, 1)
v1 - v2 # (2, 1)
v1 -= v2 # (2, 1)
```

<a name="mul" href="#mul">#</a> cvector <i>*</i> other : <i>CVector</i>

Multiply a vector by a scalar.

```py
from charming import CVector

v =CVector(2, 3)
v * 2 # (4, 6)
2 * v # (4, 6)
-v # (-2, -3)
v *= 2 #(4, 6)
```

<a name="div" href="#div">#</a> cvector */* other: *CVector*

Divide a vector by a scalar.

```py
from charming import CVector

v = CVector(2, 4)
v / 2 # (1.0, 2.0)
v /= 2 # (1.0, 2.0)
```

<a name="dist" href="#dist">#</a> cvector.**dist**(*cvector*) : *number*

Calculate the distance between two points.

```py
from charming import CVector

v1 = CVector(1, 2)
v2 = CVector(4, 6)
v1.dist(v2) # 5.0
```

<a name="dot" href="#dot">#</a> cvector.**dot**(*cvector*) : *number*

Calculate the dot product of two vectors.

```py
from charming import CVector

v1 = CVector(1, 2)
v2 = CVector(2, 3)
v1.dot(v2) # 8
```

<a name="cross" href="#cross">#</a> cvector.**cross**(*cvector*) : *number*

Calculate and return the cross product.

```py
from charming import CVector

v1 = CVector(1, 2)
v2 = CVector(2, 3)
v1.cross(v2) # -1
```

<a name="normalize" href="#normalize">#</a> cvector.**normalize**() : *CVector*

Normalize the vector to a length of 1.

```py
from charming import CVector
from math import isclose

v = CVector(3, 4)
isclose(v.normalize().mag, 1.0) # True
```

<a name="limit" href="#limit">#</a> cvector.**limit**(*max_len*) : *CVector*

Limit the magnitude of the vector.

```py
from charming import CVector

v = CVector(3, 4)
v.limit(6).mag # 5.0
v.limit(4).mag # 4.0
```

<a name="set_mag" href="#set_mag">#</a> cvector.mag **=** *number* : *CVector*

Set the magnitude of the vector.

```py
from charming import CVector
from math import isclose

v = CVector(3, 4)
v.mag = 2
isclose(v.mag, 2) # True
```

<a name="heading" href="#heading">#</a> cvector.**heading**(*max_len*) : *number*

Calculate the angle of rotation for this vector.

```py
from charming import CVector
from math import pi, isclose

v = CVector(1, 1)
isclose(v.heading(), pi / 4) # True
```

<a name="rotate" href="#rotate">#</a> cvector.**rotate**(*theta*) : *CVector*

Rotate the vector by an angle (2D only)

```py
from charming import CVector
from math import pi, isclose

v = CVector(1, 1)
isclose(v.rotate(pi / 2).heading(), pi / 4 + pi / 2) # True
```

<a name="lerp" href="#lerp">#</a> cvector.**lerp**(*cvector*, *amt*) : *CVector*

Linear interpolate the vector to another vector.

```py
from charming import CVector
from math import isclose

v1 = CVector(1, 2)
v2 = CVector(2, 3)
v3 = v1.lerp(v2, 0.4)

isclose(v3.x, 1.4) # True
isclose(v3.y, 2.4) # True
```

<a name="angle_between" href="#angle_between">#</a> cvector.**angle_between**(*cvector*) : *number*

Calculate and return the angle between two vectors.

```py
from charming import CVector
from math import pi, isclose

v1 = CVector.from_angle(pi / 4)
v2 = CVector.from_angle(pi / 3)
angle = v1.angle_between(v2)
isclose(angle, pi / 3 - pi / 4) # True
```

<a name="array" href="#array">#</a> cvector.**array**() : *list*

Return a representation of the vector as a float array.

```py
from charming import CVector

v = CVector(1, 2)
v.array() # [1, 2]
```

## Calculation

- `abs(n)`
- `ceil(n)`
- `constrain(amt, low, high)`
- `dist(x1, y1, x2, y2)`
- `exp(n)`
- `floor(n)`
- `lerp(start, stop, amt)`
- `log(x)`
- `mag(a, b, c=0)`
- `map(value, start1, stop1, start2, stop2)`
- `max(arg1, arg2, *args[, key])`
- `min(arg1, arg2, *args[, key])`
- `norm(value, start, stop)`
- `pow(n, e)`
- `round(n)`
- `sq(n)`
- `sqrt(n)`

## Trigonometry

- `acos(n)`
- `asin(n)`
- `atan(n)`
- `atan2(y, x)`
- `cos(n)`
- `degrees(n)`
- `radians(n)`
- `sin(n)`
- `tan(n)`

## Random

- `noise(x, y=0, z=0)`
- `noise_detail(octaves=4, falloff=0.5)`
- `noise_seed(seed)`
- `random(low[, high])`
- `random_gaussian()`
- `random_seed(seed)`

## Examples

- [Source](https://github.com/charming-art/charming/blob/master/src/cmath.py)
- [Random](https://github.com/charming-art/charming/blob/master/tests/test_math_random.py)