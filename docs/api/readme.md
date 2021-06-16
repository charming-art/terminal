# API Reference

Charming implements most of Processing's APIs related to 2D, all of the supported APIs are list below. You can take [Processing Documentation](https://processing.org/reference/) as a reference, and take a look at some basic [test samples](https://github.com/charming-art/charming/blob/master/tests/) to be familiar with the supported APIs.

- [Color](./color.md)
- [Constant](./constant.md)
- [Environment](./environment.md)
- [Event](./event.md)
- [Helper](./helper.md)
- [Image](./image.md)
- [Math](./math.md)
- [Shape](./shape.md)
- [Structure](./structure.md)
- [Time](./time.md)
- [Transform](./transform.md)
- [Typography](./typography.md)

## Color

Methods for creating, reading and setting colors.

- [cm.CColor](./color.md#ccolor) - Creates colors for storing in variables of the color datatype.
- [cm.background](./color.md#background) - Sets the color used for the background of terminal.
- [cm.fill](./color.md#fill) - Sets the color used to fill shapes.
- [cm.no_fill](./color.md#no_fill) - Disables filling shapes.
- [cm.no_stroke](./color.md#no_stroke) - Disables drawing the stroke (outline).
- [cm.stroke](./color.md#stroke) - Sets the color used to draw lines and borders around shapes.
- [cm.color_mode](./color.md#color_mode) - Changes the way Charming interprets color data.
- [cm.lerp_color](./color.md#lerp_color) - Blends two colors to find a third color somewhere between them.

## Math

Methods related to math.

### CVector

Methods for manipulation vector object which is useful for simulating physic system.

- [cm.CVector](./math.md#cvector) - A class to describe a two dimensional vector, specifically a Euclidean (also known as geometric) vector.
- [CVector.random_2D](./math.md#random_2D) - Make a new 2D unit vector with a random direction.
- [CVector.from_angle](./math.md#from_angle) - Make a new 2D unit vector from an angle.
- [cvector.set](./math.md#set) - Set the components of the vector.
- [cvector.copy](./math.md#copy) - Get a copy of the vector.
- [cvector.mag](./math.md#mag) - Calculate the magnitude of the vector.
- [cvector.mag_sq](./math.md#mag-sq) - Calculate the magnitude of the vector, squared.
- [cvector + other](./math.md#add) - Adds x and y components to a vector, one vector to another, or two independent vectors .
- [cvector - other](./math.md#sub) - Subtract x and y components from a vector, one vector from another, or two independent vectors.
- [cvector * other](./math.md#mult) - Multiply a vector by a scalar  .
- [cvector / other](./math.md#div) - Divide a vector by a scalar.
- [cvector.dist](./math.md#dist) - Calculate the distance between two points.
- [cvector.dot](./math.md#dot) - Calculate the dot product of two vectors.
- [cvector.cross](./math.md#cross) - Calculate and return the cross product.
- [cvector.normalize](./math.md#normalize) - Normalize the vector to a length of 1.
- [cvector.limit](./math.md#limit) - Limit the magnitude of the vector.
- [cvector.mag = number](./math.md#set_mag) - Set the magnitude of the vector.
- [cvector.heading](./math.md#heading) - Calculate the angle of rotation for this vector.
- [cvector.rotate](./math.md#rotate) - Rotate the vector by an angle.
- [cvector.lerp](./math.md#lerp) - Linear interpolate the vector to another vector.
- [cvector.angle_between](./math.md#angle-between) - Calculate and return the angle between two vectors.
- [cvector.array](./math.md#array) - Return a representation of the vector as a float array.

### Calculation

- [cm.abs](./math.md#abs) - Calculates the absolute value (magnitude) of a number. The absolute value of a number is always positive.
- [cm.ceil](./math.md#ceil) - Calculates the closest int value that is greater than or equal to the value of the parameter.
- [cm.constrain](./math.md#constrain) - Constrains a value to not exceed a maximum and minimum value.
- [cm.dist](./math.md#dist) - Calculates the distance between two points.
- [cm.exp](./math.md#exp) - Returns Euler's number e (2.71828...) raised to the power of the n parameter.
- [cm.floor](./math.md#floor) - Calculates the closest int value that is less than or equal to the value of the parameter.
- [cm.lerp](./math.md#lerp) - Calculates a number between two numbers at a specific increment.
- [cm.log](./math.md#log) - Calculates the natural logarithm (the base-e logarithm) of a number.
- [cm.mag](./math.md#mag) - Calculates the magnitude (or length) of a vector.
- [cm.map](./math.md#map) - Re-maps a number from one range to another.
- [cm.max](./math.md#max) - Determines the largest value in a sequence of numbers, and then returns that value.
- [cm.min](./math.md#min) - Determines the smallest value in a sequence of numbers, and then returns that value.
- [cm.norm](./math.md#norm) - Normalizes a number from another range into a value between 0 and 1.
- [cm.pow](./math.md#pow) - Facilitates exponential expressions.
- [cm.round](./math.md#round) - Calculates the integer closest to the n parameter.
- [cm.sq](./math.md#sq) - Squares a number (multiplies a number by itself).
- [cm.sqrt](./math.md#sqrt) - Calculates the square root of a number.

### Trigonometry

- [cm.acos](./math.md#acos) - The inverse of cos(), returns the arc cosine of a value.
- [cm.asin](./math.md#asin) - The inverse of sin(), returns the arc sine of a value.
- [cm.atan](./math.md#atan) - The inverse of tan(), returns the arc tangent of a value.
- [cm.atan2](./math.md#atan2) - Calculates the angle (in radians) from a specified point to the coordinate origin as measured from the positive x-axis.
- [cm.cos](./math.md#cos) - Calculates the cosine of an angle.
- [cm.degrees](./math.md#degrees) - Converts a radian measurement to its corresponding value in degrees.
- [cm.radians](./math.md#radians) - Converts a degree measurement to its corresponding value in radians.
- [cm.sin](./math.md#sin) - Calculates the sine of an angle.
- [cm.tan](./math.md#tan) - Calculates the ratio of the sine and cosine of an angle.

### Random

- [cm.noise](./math.md#noise) - Returns the Perlin noise value at specified coordinates.
- [cm.noise_detail](./math.md#noise-detail) - Adjusts the character and level of detail produced by the Perlin noise function.
- [cm.noise_seed](./math.md#noise-seed) - Sets the seed value for noise().
- [cm.random](./math.md#random) - Generates random numbers.
- [random_gaussian](./math.md#random-gaussian) - Returns a float from a random series of numbers having a mean of 0 and standard deviation of 1.
- [random_seed](./math.md#random-seed) - Sets the seed value for random().

## Time

Methods for returning information about current time.

- [cm.day](./time.md#day) - The day() function returns the current day as a value from 1 - 31.
- [cm.hour](./time.md#hour) - The hour() function returns the current hour as a value from 0 - 23.
- [cm.millis](./time.md#millis) - Returns the number of milliseconds (thousandths of a second) since starting the program.
- [cm.minute](./time.md#minute) - The minute() function returns the current minute as a value from 0 - 59.
- [cm.month](./time.md#month) - The month() function returns the current month as a value from 1 - 12.
- [cm.second](./time.md#second) - The second() function returns the current second as a value from 0 - 59.
- [cm.year](./time.md#year) - The year() function returns the current year as an integer (2003, 2004, 2005, etc).
