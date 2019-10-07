import time, os
from p3.core.var import *

def run(config):
	'''the enter of the program'''
	global sleep_time
	os.system('clear')
	config['setup']()
	while True:
		config['draw']()
		time.sleep(sleep_time)



