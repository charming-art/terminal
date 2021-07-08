import charming as cm

cm.full_screen()
cm.no_cursor()

img = cm.CImage(100, 100)
img.load_pixels()
for i in range(img.width):
    for j in range(img.height):
        img.set(i, j, (255, 0, 0, 1))
img.update_pixels()
cm.image(img, 0, 0, 10, 5)

cm.run()
