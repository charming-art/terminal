# Structure

Like there are static mode for static effects and active mode for dynamic effects in Processing, you can also use them in Charming but with a little difference.

## Static mode

In Processing, you needn't import APIs or call an extra method to run the sketch, but you need import APIs at first and call an extra method `run` to run the sketch in Charming.

### Processing

```java
/* processing code: static mode */

size(900, 300);
rect(0, 0, 100, 150);
```

![processnig structure](https://raw.githubusercontent.com/charming-art/public-files/master/processing_structure_static.png)

### Charming

```python
''' charming code: static mode '''

# import APIs
import charming as app

app.full_screen()
app.rect(0, 0, 10, 10)

# run sketch
app.run()
```

![processnig static structure](https://raw.githubusercontent.com/charming-art/public-files/master/structure_static.png)

## Active mode

Processing will automatically run the `setup` and `draw` functions you defined, but Charming will run them only they have been registered by specific decorators.

### Processing

```java
/* processing code: active mode */

void setup() {
    size(900, 300);
}

int x = 0;

void draw() {
    background(0);
    x += 1;
    rect(x, 0, 100, 150);
}
```

![processnig active structure](https://raw.githubusercontent.com/charming-art/public-files/master/processing_structure_active.gif)

### Charming

```py
''' charming code: active mode '''

import charming as app

@app.setup
def setup():
    app.full_screen()

x = 0

@app.draw
def draw():
    app.background(' ')
    global x
    x += 1
    app.rect(x, 0, 10, 10)

app.run()
```

![active structure](https://raw.githubusercontent.com/charming-art/public-files/master/structure_active.gif)