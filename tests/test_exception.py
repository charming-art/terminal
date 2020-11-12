import charming as app

@app.setup
def steup():
    app.full_screen()

@app.draw
def draw():
    app.rect()

app.run()

# app.full_screen()
# app.rect()
# app.run()