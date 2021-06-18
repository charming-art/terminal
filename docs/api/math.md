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

<a name="abs" href="#abs">#</a> cm.**abs**(*n*) : *number*

Calculates the absolute value (magnitude) of a number.

```py
from charming import abs

abs(1) # 1
abs(-1) # 1
abs(0) # 0
```

<a name="ceil" href="#ceil">#</a> cm.**ceil**(*n*) : *number*

Calculates the closest int value that is greater than or equal to the value of the parameter.

```py
from charming import ceil

ceil(1.2) # 2
ceil(-1.2) # -1
ceil(1) # 1
ceil(-1) # -1
```

<a name="constrain" href="#constrain">#</a> cm.**constrain**(*amt*, *low*, *high*) : *number*

Constrains a value to not exceed a maximum and minimum value.

```py
from charming import constrain

constrain(-1, 2, 3) # 2
constrain(4, 2, 3) # 3
constrain(2.5, 2, 3) # 2.5
```

<a name="dist" href="#dist">#</a> cm.**dist**(*x*1, *y1*, *x2*, *y2*) : *number*

Calculates the distance between two points.

```py
from charming import dist

dist(0, 0, 1, 0) # 1.0
dist(-1, -1, 2, 3) # 5.0
```

<a name="exp" href="#exp">#</a> cm.**exp**(*n*) : *number*

Returns Euler's number e (2.71828...) raised to the power of the n parameter.

```py
from charming import exp

exp(1) # 2.718281828459045
```

<a name="floor" href="#floor">#</a> cm.**floor**(*n*) : *number*

Calculates the closest int value that is less than or equal to the value of the parameter.

```py
from charming import floor

floor(1.2) # 1
floor(-1.2) # -2
floor(0) # 0
```

<a name="lerp" href="#lerp">#</a> cm.**lerp**(*start*, *stop*, *amt*) : *number*

Calculates a number between two numbers at a specific increment.

```py
from charming import lerp

lerp(1, 2, 0) # 1
lerp(1, 2, 1) # 2
lerp(10, 20, 0.2) # 12.0
```

<a name="log" href="#log">#</a> cm.**log**(*n*) : *number*

Calculates the natural logarithm (the base-e logarithm) of a number.

```py
from charming import log

log(math.e) # 1.0
```

<a name="mag" href="#mag">#</a> cm.**mag**(*a*, *b*, *c*=0) : *number*

Calculates the magnitude (or length) of a vector.

```py
from charming import mag

mag(3, 4) # 5.0
mag(3, 4, 12) # 13.0
```

<a name="map" href="#map">#</a> cm.**map**(*value*, *start1*, *stop1*, *start2*, *stop2*) : *number*

Re-maps a number from one range to another.

```py
from charming import map

map(1.5, 1, 2, 10, 20) # 15
```

<a name="max" href="#max">#</a> cm.**max(*\*args*, *\*\*kw*)** : *number*

Determines the largest value in a sequence of numbers, and then returns that value.

```py
from charming import max

max(0, 1) # 1
max(0, 1, 2) # 2
max([0, 1, 2, 3]) # 3
```

<a name="min" href="#min">#</a> cm.**max(*\*args*, *\*\*kw*)** : *number*

Determines the smallest value in a sequence of numbers, and then returns that value.

```py
from charming import min

min(0, 1) # 0
min(0, 1, 2) # 0
min([0, 1, 2, 3]) # 0
```

<a name="norm" href="#norm">#</a> cm.**norm**(*value*, *start*, *stop*) : *number*

Normalizes a number from another range into a value between 0 and 1.

```py
from charming import norm

norm(20, 0, 50) # 0.4
```

<a name="pow" href="#pow">#</a> cm.**pow**(*n*, *e*) : *number*

Facilitates exponential expressions.

```py
from charming import pow

pow(3, 2) # 9.0
pow(4, 0.5) # 2.0
```

<a name="round" href="#round">#</a> cm.**round**(*n*) : *number*

Calculates the integer closest to the n parameter.

```py
from charming import round

round(9.2) # 9
round(9.4) # 9
round(9.5) # 10
round(-1.4) # -1
round(-1.5) # -2
```

<a name="sq" href="#sq">#</a> cm.**sq**(*n*) : *number*

Squares a number (multiplies a number by itself).

```py
from charming import sq

sq(5) # 25
```

<a name="sqrt" href="#sqrt">#</a> cm.**sqrt**(*n*) : *number*

Calculates the square root of a number.

```py
from charming import sqrt

sqrt(25) # 5.0
```

## Trigonometry

<a name="acos" href="#acos">#</a> cm.**acos**(*n*) : *number*

The inverse of cos(), returns the arc cosine of a value.

```py
from charming import acos

acos(0.5) # math.pi / 3
```

<a name="asin" href="#asin">#</a> cm.**asin**(*n*) : *number*

The inverse of sin(), returns the arc sine of a value.

```py
from charming import asin

acos(1) # math.pi / 2
```

<a name="atan" href="#atan">#</a> cm.**atan**(*n*) : *number*

The inverse of tan(), returns the arc tangent of a value.

```py
from charming import atan

atan(1) # math.pi / 4
```

<a name="atan2" href="#atan2">#</a> cm.**atan2**(*y*, *x*) : *number*

Calculates the angle (in radians) from a specified point to the coordinate origin as measured from the positive x-axis.

```py
from charming import atan2

atan2(1, 1) # math.pi / 4
```

<a name="cos" href="#cos">#</a> cm.**cos**(*n*) : *number*

Calculates the cosine of an angle.

```py
from charming import cos
from charming import PI

cos(PI / 3) # 0.5
```

<a name="degrees" href="#degrees">#</a> cm.**degrees**(*n*) : *number*

Converts a radian measurement to its corresponding value in degrees.

```py
from charming import degrees
from charming import PI

degrees(PI) # 180.0
```

<a name="radians" href="#radians">#</a> cm.**degrees**(*n*) : *number*

Converts a degree measurement to its corresponding value in radians.

```py
from charming import radians

radians(180.0) # math.pi
```

<a name="sin" href="#sin">#</a> cm.**sin**(*n*) : *number*

Calculates the sine of an angle.

```py
from charming import sin
from charming import PI

sin(PI / 6) # 0.5
```

<a name="tan" href="#tan">#</a> cm.**tan**(*n*) : *number*

Calculates the ratio of the sine and cosine of an angle

```py
from charming import tan
from charming import PI

tan(PI / 4) # 1
```

## Random

- `noise(x, y=0, z=0)`
- `noise_detail(octaves=4, falloff=0.5)`
- `noise_seed(seed)`
- `random(low[, high])`
- `random_gaussian()`
- `random_seed(seed)`