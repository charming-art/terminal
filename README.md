# Cell

The creative language for ASCII art based on Basic.

> [!NOTE]
> The current next branch is implementing the new proposal API for production use. Please refer to the [python branch](https://github.com/charming-art/charming-cell/tree/python) for the released Python version.

## Get Started

```bash
$ cell hello.cll
```

```
LET x = 0

Draw:
  BACKGROUND 0
  STROKE '0', YELLOW, RED
  FILL 'X', GREEN, BLUE
  RECT x, 0, 0
  LET x = x + 1
```

## License 📄

ISC@Bairui SU
