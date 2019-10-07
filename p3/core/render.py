from p3.core.var import *
import os

def rect(x, y, width, height):
	'''draw a rect to the screen'''
	global stroke_char
	if width < 2 or height < 2:
		return
	result = y * '\n'
	for j in range(height):

		row_char = stroke_char
		## 第一排和最后一排
		if not j == 0 and not j == height - 1:
			row_char = fill_char
		result += x * ' ' + stroke_char + (width - 2) * row_char + stroke_char + '\n'
	print(result)


def stroke(char):
	global stroke_char
	stroke_char = char

def fill(char):
	global fill_char
	fill_char = char

def background(char):
	os.system('clear')

def noFill():
	fill(' ')

def noStoke():
	stroke(' ')
