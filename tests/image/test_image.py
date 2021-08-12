import charming as cm

cm.full_screen()
cm.no_cursor()

img = cm.load_image('../assets/images/test.png')
cm.image(img, 0, 0, 30, 15)

cm.run()
