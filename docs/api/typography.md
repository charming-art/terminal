# Typography

<a name="text" href="#text">#</a> cm.**text**(*text*, *x*, *y*)

Draws text to the screen. Displays the information specified in the first parameter on the screen in the position specified by the additional parameters.

A default font will be used unless a font is set with the text_font() function and a default size will be used unless a font is set with text_size(). Change the color of the text with the stroke() function. The text displays in relation to the text_align() function, which gives the option to draw to the left, right, and center of the coordinates.

```py
import charming as cm

# If you want to draw a ascii text, you'd
# better use raw string: r'''xxx'''.
head = r'''
         .-"""-.
        /       \
        \       /
 .-"""-.-`.-.-.<  _
/      _,-\ ()()_/:)
\     / ,  `     `|
 '-..-| \-.,___,  /
       \ `-.__/  /
        `-.__.-'`
'''

face = "(^O^)/"

cm.full_screen()
cm.no_cursor()

cm.stroke(fg=cm.RED, bg=cm.YELLOW)
cm.text(head, 0, 0)
cm.text(face, 25, 5)

cm.stroke_weight(1)
cm.text('h', 35, 5)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_text.png" />

<a name="text_width" href="#text_width">#</a> cm.**text_width**(*text*) : *number*

Calculates and returns the width of any character or text string.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

text = 'charming'
width = cm.get_width()

th1 = cm.text_height(text)
cm.text(text, (width - cm.text_width(text)) / 2, 0)

cm.text_size(cm.BIG)
th2 = cm.text_height(text)
cm.text(text, (width - cm.text_width(text)) / 2, th1)

cm.text_size(cm.LARGE)
cm.text(text, (width - cm.text_width(text)) / 2, th1 + th2)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_text_width.png" />

<a name="text_align" href="#text_align">#</a> cm.**text_align**(*align_x*=LEFT | RIGHT | CENTER[, *align_y*=TOP | BOTTOM | MIDDLE])

Sets the current alignment for drawing text.The parameters LEFT, CENTER, and RIGHT set the display characteristics of the letters in relation to the values for the x and y parameters of the text() function.

```py
import charming as cm

text = 'charming'

cm.full_screen()
cm.no_cursor()
cm.translate(cm.get_width() / 2, cm.get_height() / 2)

cm.stroke('|')
cm.line(0, -cm.get_height() / 2, 0, cm.get_height() / 2)

# left
cm.text_align(cm.LEFT)
cm.text(text, 0, -5)

# center
cm.text_align(cm.CENTER)
cm.text(text, 0, 0)

# right
cm.text_align(cm.RIGHT)
cm.text(text, 0, 5)


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_text_align_x.png" />

```py
import charming as cm

text = 'ch'

cm.full_screen()
cm.no_cursor()
cm.translate(cm.get_width() / 2, cm.get_height() / 2)

cm.stroke('-')
cm.line(-cm.get_width() / 2, 0, cm.get_width() / 2, 0)
cm.text_size(cm.BIG)

# top
cm.text_align(cm.CENTER, align_y=cm.TOP)
cm.text(text, -20, 0)

# middle
cm.text_align(align_y=cm.MIDDLE)
cm.text(text, 0, 0)

# bottom
cm.text_align(align_y=cm.BOTTOM)
cm.text(text, 20, 0)


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_text_align_y.png" />

<a name="text_size" href="#text_size">#</a> cm.**text_size**(*size*=NORMAL | BIG |LARGE))

Sets the current font size.

```py
import charming as cm

text = 'charming'

cm.full_screen()
cm.no_cursor()

cm.text(text, 0, 0)

cm.text_size(cm.BIG)
cm.text(text, 0, 2)

cm.text_size(cm.LARGE)
cm.text(text, 0, 8)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_text_size.png" />

<a name="text_height" href="#text_height">#</a> cm.**text_height**(*text*) : *number*

Calculates and returns the height of any character or text string.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()

text = 'C'
height = cm.get_height()
width = cm.get_width()

cm.text(text, 0, (height - cm.text_height(text)) / 2)

cm.text_size(cm.BIG)
cm.text(text, 10, (height - cm.text_height(text)) / 2)

cm.text_size(cm.LARGE)
cm.text(text, 20, (height - cm.text_height(text)) / 2)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_text_height.png" />

<a name="get_font_list" href="#get_font_list">#</a> cm.**get_font_list**(*text*, *x*, *y*) : *string[]*

Returns the supported font list for text with BIG font size.

```py
import charming as cm

font_list = cm.get_font_list()

print(font_list) # ['clb6x10', 'nipples', 'computer', ...]
print(len(font_list)) # 425
```

<a name="text_font" href="#text_font">#</a> cm.**text_font**(*name*)

Sets the current font that will be drawn with the text() function.

```py
import charming as cm

cm.full_screen()
cm.no_cursor()
cm.text_size(cm.BIG)

font_list = cm.get_font_list()
text = 'charming'

th = cm.text_height(text)
cm.text(text, 0, 0)

cm.text_font(font_list[0])
th1 = cm.text_height(text)
cm.text(text, 0, th)

cm.text_font(font_list[1])
cm.text(text, 0, th + th1)

cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_text_font.png" />