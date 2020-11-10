import charming as app

app.full_screen()
hello_world = app.figlet_text('app')
# app.stroke(fg=app.RED)
app.text(hello_world, 0, 0)
app.log(app.get_font_list())
app.run()
