# Typography

<a name="text" href="#text">#</a> cm.**text**(*text*, *x*, *y*)

Draws text to the screen. Displays the information specified in the first parameter on the screen in the position specified by the additional parameters.

A default font will be used unless a font is set with the text_font() function and a default size will be used unless a font is set with text_size(). Change the color of the text with the fill() function. Change the outline of the text with the stroke() and stroke_weight() functions.The text displays in relation to the text_align() function, which gives the option to draw to the left, right, and center of the coordinates.

<a name="text_width" href="#text_width">#</a> cm.**text_width**(*text*) : *number*

Calculates and returns the width of any character or text string.

<a name="text_align" href="#text_align">#</a> cm.**text_align**(*align_x*=LEFT | RIGHT | CENTER[, *align_y*=TOP | BOTTOM | MIDDLE])

Sets the current alignment for drawing text.The parameters LEFT, CENTER, and RIGHT set the display characteristics of the letters in relation to the values for the x and y parameters of the text() function.

<a name="text_size" href="#text_size">#</a> cm.**text_size**(*size*=NORMAL | BIG |LARGE))

Sets the current font size.

<a name="text_height" href="#text_height">#</a> cm.**text_height**(*text*) : *number*

Calculates and returns the height of any character or text string.

<a name="get_font_list" href="#get_font_list">#</a> cm.**get_font_list**(*text*, *x*, *y*) : *string[]*

Returns the supported font list for terminal.

<a name="text_font" href="#text_font">#</a> cm.**text_font**(*name*)

Sets the current font that will be drawn with the text() function.

## Examples

- [ascii](https://github.com/charming-art/charming/blob/master/tests/test_typography_ascii.py)
- [words](https://github.com/charming-art/charming/blob/master/tests/test_typography_words.py)
- [clock](https://github.com/charming-art/charming/blob/master/tests/test_time.py)