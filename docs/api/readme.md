# API Reference

Charming implements most of Processing's APIs related to 2D, all of the supported APIs are list below. Noticed that the API reference for Charming copies most of [Processing's API reference](https://processing.org/reference/) but replace examples and some features for Charming.

- [Color](#color)
- [Constants](#constants)
- [Helpers](#helpers)
- [Image](#image) ([CImage](#cimage), [Display](#display))
- [Environment](#environment)
- [Events](#events) ([Keyboard](#keyboard), [Mouse](#mouse), [Cursor](#cursor))
- [IO](#io)
- [Math](#math) ([CVector](#cvector), [Calculation](#calculation), [Trigonometry](#trigonometry), [Random](#random))
- [Structure](#structure)
- [Shape](#shape) ([2D Primitives](#2D-Primitives), [Attributes](#attributes), [Vertex](#vertex), [Curves](#curves))
- [Time](#time)
- [Transform](#transform)
- [Typography](#typography)

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

## Constants

Constants for angle.

- [cm.PI](./constants.md#PI) - PI is a mathematical constant with the value 3.1415927.
- [cm.HALF_PI](./constants.md#HALF_PI) - HALF_PI is a mathematical constant with the value 1.5707964.
- [cm.QUARTER_PI](./constants.md#QUARTER_PI) - QUARTER_PI is a mathematical constant with the value 0.7853982.
- [cm.TAU](./constants.md#TAU) - TAU is a mathematical constant with the value 6.2831855.
- [cm.TWO_PI](./constants.md#TWO_PI) - TWO_PI is a mathematical constant with the value 6.2831855.
  
## Helpers

Methods for improving programming efficiency.

- [cm.print](./helpers.md#print) - Print output to file to debug.
- [cm.check_params](./helpers.md#check_params) - Checks the type of params to output the potential error.

## Image

Methods for drawing image to screen.

### CImage

Date type for Charming to store and manipulate image.

- [cm.CImage](./image.md#cimage) - Creates a new CImage (the datatype for storing images).
- [CImage.load_pixels](./image.md#load_pixels) - Loads the pixels data for this image into the `pixels` attribute.
- [CImage.update_pixels](./image.md#update_pixels) - Updates the backing canvas for this image with the contents of the `pixels` array.
- [CImage.set](./image.md#set) - Set the color of a single pixel.
- [CImage.get](./image.md#get) - Get the color of a single pixel.

### Display

Methods for display images.

- [cm.image](./image.md#image) - Draw an image to the charming canvas.
- [cm.image_mode](./image.md#image_mode) - Set image mode.
- [cm.load_image](./image.md#load_image) - Loads an image from a path and creates a CImage from it.
- [cm.no_tint](./image.md#no_tint) - Removes the current fill value for displaying images.
- [cm.tint](./image.md#tint) - Sets the fill value for displaying images.

## Environment

Methods for set and get runtime environment.

- [cm.cursor](./environment.md#cursor) - Set the cursor visible.
- [cm.set_cursor](./environment.md#set_cursor) - Set the positions of cursor in cells.
- [cm.no_cursor](./environment.md#no_cursor) - Hide the cursor.
- [cm.frame_rate](./environment.md#frame_rate) - Specifies the number of frames to be displayed every second.
- [cm.full_screen](./environment.md#full_screen) - Sets the sketch to fill the entire terminal.
- [cm.get_frame_count](./environment.md#get_frame_count) - The system variable frame_count contains the number of frames that have been displayed since the program started.
- [cm.get_height](./environment.md#get_height) - System variable that stores the height of the drawing canvas.
- [cm.get_width](./environment.md#get_width) - System variable that stores the width of the drawing canvas.
- [cm.size](./environment.md#size) - Sets the dimensions of it in cells for the sketch.

## Events

Methods for listening and handling events.

### Keyboard

Methods for keyboard events.

- [cm.get_key](./events.md#get_key) - The system variable key always contains the value of the most recent key on the keyboard that was used (either pressed or released).
- [cm.get_key_code](./events.md#get_key_code) - The variable keyCode is used to detect special keys such as the arrow keys (UP, DOWN, LEFT, and RIGHT) as well as ENTER, SPACE.
- [cm.get_key_pressed](./events.md#get_key_pressed) - The boolean system variable key_pressed is true if any key is pressed and false if no keys are pressed.
- [cm.key_pressed](./events.md#key_pressed) - The function decorated by key_pressed decorator is called once every time a key is pressed.
- [cm.key_released](./events.md#key_released) - The function decorated by key_released decorator is called once every time a key is released.
- [cm.key_typed](./events.md#key_typed) - The function decorated by key_typed decorator is called once every time a key is typed.

### Mouse

Methods for mouse events.

- [cm.get_mouse_x](./events.md#get_mouse_x) - The system variable mouse_x always contains the current horizontal coordinate of the mouse.
- [cm.get_mouse_y](./events.md#get_mouse_y) - The system variable mouse_y always contains the current vertical coordinate of the mouse.
- [cm.get_mouse_pressed](./events.md#get_mouse_pressed) - The mouse_pressed variable stores whether or not a mouse button is currently being pressed.
- [cm.get_mouse_button](./events.md#get_mouse_button) - When a mouse button is pressed, the value of the system variable mouseButton is set to either LEFT, RIGHT, or CENTER, depending on which button is pressed.
- [cm.mouse_clicked](./events.md#mouse_clicked) - The function decorated mouse_clicked decorator is called after a mouse button has been pressed and then released.
- [cm.mouse_pressed](./events.md#mouse_pressed) - The function decorated mouse_released decorator is called after a mouse button has been pressed.
- [cm.mouse_released](./events.md#mouse_released) - The function decorated mouse_released decorator is called after a mouse button has been released.

### Cursor

Methods for cursor events.

- [cm.get_cursor_x](./events.md#get_cursor_x) - The system variable cursor_x always contains the current horizontal coordinate of the cursor.
- [cm.get_cursor_y](./events.md#get_cursor_y) - The system variable cursor_y always contains the current vertical coordinate of the cursor.
- [cm.get_pcursor_x](./events.md#get_pcursor_x) - The system variable pcursor_x always contains the horizontal position of the cursor in the frame previous to the current frame.
- [cm.get_pcursor_y](./events.md#get_pcursor_y) - The system variable pcursor_y always contains the vertical position of the cursor in the frame previous to the current frame.
- [cm.cursor_moved](./events.md#cursor_moved) - The function decorated cursor_moved decorator is called after a cursor moved.
- [cm.cursor_pressed](./events.md#cursor_pressed) - The function decorated cursor_pressed decorator is called after a cursor pressed.
- [cm.get_cursor_moved](./events.md#get_cursor_moved) - The boolean system variable cursor_moved is true if any cursor is pressed and false if cursor is not pressed.

## IO

Methods for IO.

- [cm.load_json](./io.md#load_json) - Loads data from JSON file to dict object.
- [cm.load_csv](./io.md#load_csv) - Loads data from CSV file to dict object.

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

Methods for basic math calculation.

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

Methods for calculate trigonometry.

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

Methods for generate random numbers.

- [cm.noise](./math.md#noise) - Returns the Perlin noise value at specified coordinates.
- [cm.noise_detail](./math.md#noise-detail) - Adjusts the character and level of detail produced by the Perlin noise function.
- [cm.noise_seed](./math.md#noise-seed) - Sets the seed value for noise().
- [cm.random](./math.md#random) - Generates random numbers.
- [cm.random_gaussian](./math.md#random-gaussian) - Returns a float from a random series of numbers having a mean of 0 and standard deviation of 1.
- [cm.random_seed](./math.md#random-seed) - Sets the seed value for random().

## Structure

Methods for controlling the running flow of sketch.

- [cm.setup](./structure.md#setup) - The function decorated by setup() decorator is called once when the program starts.
- [cm.draw](./structure.md#draw) - The function decorated by draw() called directly after setup(), it continuously executes the lines of code contained inside its block until the program is stopped or no_loop() is called.
- [cm.run](./structure.md#run) - Run the sketch or nothing magic will happen.
- [cm.no_loop](./structure.md#no_loop) - Stops Charming from continuously executing the code within draw().
- [cm.loop](./structure.md#loop) - The draw() loop may be stopped by calling no_loop(). In that case, the draw() loop can be resumed with loop().
- [cm.get_is_looping](./structure.md#get_is_looping) - get_is_looping() returns the current state for use within custom event handlers.
- [cm.redraw](./structure.md#redraw) - Executes the code within draw() one time.
- [cm.push](./structure.md#push) - The push() function saves the current drawing style settings and transformations, while pop() restores these settings.
- [cm.pop](./structure.md#pop) - The push() function saves the current drawing style settings and transformations, while pop() restores these settings.
- [cm.open_context](./structure.md#open_context) - The syntactic sugar for push() and pop().
- [cm.exit](./structure.md#exit) - Exit the sketch.

## Shape

Methods for drawing shapes.

### 2D Primitives

Methods for drawing 2D basic shapes.

- [cm.arc](./shape.md#arc) - Draws an arc to the screen. Arcs are drawn along the outer edge of an ellipse defined by the a, b, c, and d parameters.
- [cm.circle](./shape.md#circle) - Draws a circle to the screen. By default, the first two parameters set the location of the center, and the third sets the shape's width and height.
- [cm.ellipse](./shape.md#ellipse) - Draws an ellipse (oval) to the screen. An ellipse with equal width and height is a circle.
- [cm.line](./shape.md#line) - Draws a line (a direct path between two points) to the screen.
- [cm.point](.shape.md#point) - Draws a point, a coordinate in space at the dimension of one cell.
- [cm.quad](./shape.md#quad) - A quad is a quadrilateral, a four sided polygon.
- [cm.rect](./shape.md#rect) - Draws a rectangle to the screen. A rectangle is a four-sided shape with every angle at ninety degrees.
- [cm.square](./shape.md#square) - Draws a square to the screen.
- [cm.triangle](./shape.md#triangle) - A triangle is a plane created by connecting three points
  
### Attributes

Methods for setting drawing attributes.

- [cm.ellipse_mode](./shape.md#ellipse_mode) - Modifies the location from which ellipses are drawn by changing the way in which parameters given to ellipse() are interpreted.
- [cm.rect_mode](./shape.md#rect_mode) - Modifies the location from which rectangles are drawn by changing the way in which parameters given to rect() are interpreted.
- [cm.stroke_weight](./shape.md#stroke_weight) - Sets the width of the stroke used for lines, points, and the border around shapes.

### Vertex

Methods for drawing custom shapes.

- [cm.begin_shape](./shape.md#begin_shape) - Using the begin_shape() and end_shape() functions allow creating more complex forms.
- [cm.end_shape](./shape.md#end_shape) - The end_shape() function is the companion to begin_shape() and may only be called after beginShape().
- [cm.open_shape](./shape.md#open_shape) - The syntax sugar for begin_shape and end_shape.
- [cm.vertex](./shape.md#vertex) - All shapes are constructed by connecting a series of vertices.
- [cm.begin_contour](./shape.md#begin_contour) - Use the begin_contour() and end_contour() function to create negative shapes within shapes such as the center of the letter 'O'.
- [cm.end_contour](./shape.md#end_contour) - Use the begin_contour() and end_contour() function to create negative shapes within shapes such as the center of the letter 'O'.
- [cm.open_contour](./shape.md#open_contour) - The syntax sugar for begin_contour and end_contour.
- [cm.bezier_vertex](./shape.md#bezier_vertex) - Specifies vertex coordinates for Bezier curves.
- [cm.curve_vertex](./shape.md#curve_vertex) - Specifies vertex coordinates for curves.

### Curves

Methods for drawing curves.

- [cm.bezier](./shape.md#bezier) - Draws a Bezier curve on the screen.
- [cm.bezier_point](./shape.md#bezier_point) - Evaluates the Bezier at point t for points a, b, c, d
- [cm.bezier_tangent](./shape.md#bezier_tangent) - Calculates the tangent of a point on a Bezier curve.
- [cm.curve](./shape.md#curve) - Draws a curved line on the screen.
- [cm.curve_point](./shape.md#curve_point) - Evaluates the curve at point t for points a, b, c, d.
- [cm.curve_tangent](./shape.md#curve_tangent) - Calculates the tangent of a point on a curve. 
- [cm.curve_tightness](./shape.md#curve_tightness) - Modifies the quality of forms created with curve() and curveVertex().

## Time

Methods for returning information about current time.

- [cm.day](./time.md#day) - The day() function returns the current day as a value from 1 - 31.
- [cm.hour](./time.md#hour) - The hour() function returns the current hour as a value from 0 - 23.
- [cm.millis](./time.md#millis) - Returns the number of milliseconds (thousandths of a second) since starting the program.
- [cm.minute](./time.md#minute) - The minute() function returns the current minute as a value from 0 - 59.
- [cm.month](./time.md#month) - The month() function returns the current month as a value from 1 - 12.
- [cm.second](./time.md#second) - The second() function returns the current second as a value from 0 - 59.
- [cm.year](./time.md#year) - The year() function returns the current year as an integer (2003, 2004, 2005, etc).

## Transform

Methods for applying transformations to objects.

- [cm.translate](./transform.md#translate) - Specifies an amount to displace objects within the display window.
- [cm.scale](./transform.md#scale) - Increases or decreases the size of a shape by expanding or contracting vertices.
- [cm.rotate](./transform.md#rotate) - Rotates a shape by the amount specified by the angle parameter.
- [cm.shear_x](./transform.md#shear_x) - Shears a shape around the x-axis by the amount specified by the angle parameter.
- [cm.shear_y](./transform.md#shear_y) Shears a shape around the y-axis by the amount specified by the angle parameter.

## Typography

Methods for drawing expected text to screen.

- [cm.text](./typography.md#text) - Draws text to the screen.
- [cm.text_width](./typography.md#text_width) - Calculates and returns the width of any character or text string.
- [cm.text_align](./typography.md#text_align) - Sets the current alignment for drawing text.
- [cm.text_size](./typography.md#text_size) - Sets the current font size.
- [cm.text_height](./typography.md#text_height) - Calculates and returns the height of any character or text string.
- [cm.get_font_list](./typography.md#get_font_list) - Returns the supported font list for text with BIG font size.
- [cm.text_font](./typography.md#text_font) - Sets the current font that will be drawn with the text() function.
