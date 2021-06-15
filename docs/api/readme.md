# API Reference

Charming implements most of Processing's APIs related to 2D, all of the supported APIs are list below. You can take [Processing Documentation](https://processing.org/reference/) as a reference, and take a look at some basic [test samples](https://github.com/charming-art/charming/blob/master/tests/) to be familiar with the supported APIs.

- [Color](#color)
- [Constant](./constant.md)
- [Environment](./environment.md)
- [Event](./event.md)
- [Helper](./helper.md)
- [Image](./image.md)
- [Math](./math.md)
- [Shape](./shape.md)
- [Structure](./structure.md)
- [Time](./time.md)
- [Transform](./transform.md)
- [Typography](./typography.md)

## [Color](./color.md)

Methods for creating, reading and setting colors.

- [cm.CColor](./color.md#ccolor) - Creates colors for storing in variables of the color datatype.
- [cm.background](./color.md#background) - Sets the color used for the background of terminal.
- [cm.fill](./color.md#fill) - Sets the color used to fill shapes.
- [cm.no_fill](./color.md#no_fill) - Disables filling shapes.
- [cm.no_stroke](./color.md#no_stroke) - Disables drawing the stroke (outline).
- [cm.stroke](./color.md#stroke) - Sets the color used to draw lines and borders around shapes.
- [cm.color_mode](./color.md#color_mode) - Changes the way Charming interprets color data.
- [cm.lerp_color](./color.md#lerp_color) - Blends two colors to find a third color somewhere between them.
