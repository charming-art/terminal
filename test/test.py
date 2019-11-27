import p3
i = 0
def setup():
	p3.size(100, 50)
	# frameRate(0)

def draw():
	global i
	p3.background(' ')
	i += 1
	p3.stroke('¥')
	p3.fill('')
	p3.rect(2 + i, 2, 20, 10)
	if(i + 20 > p3.get_width()):
		i = 0

if __name__ == '__main__':
	p3.run({
		'setup': setup,
		'draw': draw
	})




