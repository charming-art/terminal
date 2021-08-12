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