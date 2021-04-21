# Helper

There some useful helper functions.

## Print

Because Charming use the terminal as the canvas to paint, so it is impossible for you to print some information to the console. Instead you can use the `print` function from Charming to print some information to file named `charming.log`.

### Single variable

```py
import charming as app

n = 1
app.print(n)
```

```plain text
# charming.log

DEBUG:root:1
```

### Multiple variables

```py
import charming as app

number = 123
string = 'hello'
dict = {
    'name': 'charming',
    'awesome': True
}
tuple = (1, 2)

app.print(number, string, dict, key=tuple)
```

```plain text
# charming.log
DEBUG:root:123, 'hello', {'name': 'charming', 'awesome': True}, {'key': (0, 1)}
```
