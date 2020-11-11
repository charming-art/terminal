import charming as app

img = None


@app.setup
def setup():
    global img
    app.full_screen()
    app.image_mode(app.CENTER)
    img = app.load_image('./images/test.png')


@app.draw
def draw():
    # img.load_pixels()
    # img.pixels[0] = app.color('u')
    # img.update_pixels()
    
    # app.image(img, 50, 0, 20, 10)
    # app.load_pixels()
    # pixels = app.get_pixels()
    # pixels[0] = app.color('h')
    # app.update_pixels()
    
    
    # app.image(img, 0, 0, 20, 10)
    app.translate(app.get_width() / 2, app.get_height() / 2)
    # app.rotate(app.PI)
    app.tint('+')
    app.image(img, 0, 0, 20, 10)
    # app.scale(3)
    # app.scale(3)
    
    app.no_loop()


app.run()
