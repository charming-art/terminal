# Time

Methods for returning information about current time.

<a name="day" href="#day">#</a> cm.**day**()

Returns the current day as a value from 1 - 31.

<a name="hour" href="#hour">#</a> cm.**hour**()

Returns the current hour as a value from 0 - 23.

<a name="millis" href="#millis">#</a> cm.**millis**()

Returns the number of milliseconds (thousandths of a second) since starting the program.

<a name="minute" href="#minute">#</a> cm.**minute**()

Returns the current minute as a value from 0 - 59.

<a name="month" href="#month">#</a> cm.**month**()

Returns the current month as a value from 1 - 12.

<a name="second" href="#second">#</a> cm.**second**()

Returns the current second as a value from 0 - 59.

<a name="year" href="#year">#</a> cm.**year**()

Returns the current year as an integer (2003, 2004, 2005, etc).
  
```py
import charming as cm


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()


@cm.draw
def draw():
    cm.background(' ')
    date = f'{cm.year()} . {cm.month()} . {wrap(cm.day())}'
    time = f'{wrap(cm.hour())} : {wrap(cm.minute())} : {wrap(cm.second())}'

    cm.text_align(cm.CENTER)
    cm.text_size(cm.BIG)
    h1 = cm.text_height(date)
    h = h1 + 10

    cm.translate(cm.get_width() / 2, (cm.get_height() - h) / 2)
    cm.text(date, 0, 0)
    cm.text(time, 0, 10)


def wrap(n):
    return f'0{n}' if n < 10 else n


cm.run()
```

<img src="https://raw.githubusercontent.com/charming-art/public-files/master/test_time.gif" />