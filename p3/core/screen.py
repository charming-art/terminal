from p3.core.var import *
def size(window_width, window_height):
	'''set the size of the window'''
	global width, height
	width = window_width
	height = window_height

def get_width():
	global width
	return width

def get_height():
	global height
	return height