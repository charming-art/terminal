---
id: typography
sidebar_label: Typography
hide_title: True
---

# Typography

It is as easy as Processing to display text in Charming, but only with three level of text size.

- **NORMAL**: Draw some basic words or ANSII Art to the terminal.
- **BIG**: Easily convert some normal words to ANSII Art words.
- **LARGE**: Convert some ANSII Art words to a bigger ANSII Art words.

## Normal size

```py
''' charming text: normal size '''

import charming as app

app.full_screen()

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

# draw basic texts
app.text('charming', 0, 0)

# draw some ascii art
app.text(head, 0, 5)

app.run()
```

![normal text](https://raw.githubusercontent.com/charming-art/public-files/master/text_normal.png)

## Big size

```py
''' charming text: big size '''

import charming as app

app.full_screen()

# convert basic text to ascii text
app.text_size(app.BIG)
app.text('charming', 0, 0)

# support many fonts
fonts = app.get_font_list()
app.text_font(fonts[2])
app.text('charming', 0, 10)

app.run()
```

![big text](https://raw.githubusercontent.com/charming-art/public-files/master/big_text.png)

## Large size

```py
''' charming text: normal size '''

import charming as app

app.full_screen()
app.no_cursor()

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

# convert ascii text to a lager ascii text
app.text_size(app.LARGE)
app.text(head, 0, 0)

app.run()
```

![large text](https://raw.githubusercontent.com/charming-art/public-files/master/text_large.png)
