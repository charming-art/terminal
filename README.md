# Charming

Charming is a creative coding language based on Processing and Python for character terminal art programing(charming).

## Getting Started

```py
# sketch.py
import charming as app

@app.setup
def setup():
    app.size(100, 100)

@app.draw
def draw():
    app.stroke('#')
    app.fill('@')
    app.rect(0, 0, 20, 20)

app.run()
```

### Terminal

```bash
pip3 install charming
python3 sketch.py
```

### Web

```html
<!-- index.html -->
<html>
    <head>
        <link rel="stylesheet" href="xterm.css" />
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.8.10/brython.min.js"></script>
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.8.10/brython_stdlib.js"></script>
        <script src="xterm.js"></script>
        <script type="text/python" src="charming.py"></script>
    <head>
    <body onload="brython()">
        <script type="text/python" src="sketch.py"></script>
    </body>
</html>
```

```bash
python3 - http.server 8000
```

### Online Editor

Try it one an online editor.
