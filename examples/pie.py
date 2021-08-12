import charming as cm
from scales import scale_linear, scale_ordinal


def stack(data):
    values = []
    pre = 0
    for d in data:
        d['start'] = pre
        d['end'] = pre + d['value']
        values.append(d)
        pre = d['end']
    return values


# prepare data
people = [
    {'name': 'white', 'value': 43},
    {'name': 'yellow', 'value': 41},
    {'name': 'black', 'value': 16},
]

data = stack(people)

cm.print(data)
theta = scale_linear(
    [0, people[-1]['end']],
    [-cm.HALF_PI, cm.TWO_PI - cm.HALF_PI]
)
color = scale_ordinal(list(map(lambda x: x['name'], data)), [
    cm.CColor(('🖐🏻', 2),  (91, 143, 249), (91, 143, 249)),
    cm.CColor(('🖐️', 2), (97, 221, 170), (97, 221, 170)),
    cm.CColor(('🖐🏿', 2), (255,107,59), (255,107,59)),
])


# environment
cm.full_screen(cm.DOUBLE)
cm.color_mode(cm.RGB)
cm.no_cursor()

# draw
cm.translate(cm.get_width() / 2, cm.get_height() / 2)
for d in data:
    cm.no_stroke()
    cm.fill(color(d['name']))
    cm.arc(0, 0, 18, 18, theta(d['start']), theta(d['end']), cm.PIE)

cm.run()
