import charming as app

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

app.full_screen()
app.no_cursor()
app.stroke(fg=app.YELLOW, bg=app.RED)

app.text(head, 0, 5)
app.text(face, 25, 5)
app.text_size(app.LARGE)
app.text(face, 45, 5)
app.run()
