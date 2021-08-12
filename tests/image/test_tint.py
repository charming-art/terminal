import charming as cm

cm.full_screen()
cm.no_cursor()

img = cm.load_image('../assets/images/test.png')
cm.tint('O', cm.RED)
cm.image(img, 0, 0, 30, 15)

cm.no_tint()
cm.image(img, 32, 0, 30, 15)

cm.run()