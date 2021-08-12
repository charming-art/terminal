import charming as cm

cm.full_screen()
cm.no_cursor()

img = cm.load_image('../assets/images/test.png')
img.load_pixels()
for i in range(int(img.width / 2)):
    for j in range(img.height):
        ri = img.width - i - 1
        color = img.get(i, j)
        img.set(ri, j, color)
img.update_pixels()

cm.image(img, 0, 0, 30, 15)
cm.run()
