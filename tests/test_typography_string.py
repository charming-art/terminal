import charming as app

app.full_screen(app.DOUBLE)
app.no_cursor()
texts = [
  'hello world',
  '🚀🚀h',
  'h🚀llo'
]

for i, t in enumerate(texts):
  app.text(t, 0, i)

app.run()