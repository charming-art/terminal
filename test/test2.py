import curses
import time
from curses import wrapper
stdscr = curses.initscr()
begin_x = 20; begin_y = 7
height = 5; width = 40

# win = curses.newwin(height, width, begin_y, begin_x)

i = 0
def main(stdscr):
    # Clear screen
    stdscr.refresh()
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    # for i in range(0, 11):
    #     v = i-10
    #     stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
    global i
    # i += 1
    rows, cols = stdscr.getmaxyx()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_GREEN)
    # win.keypad(1)  # Enable arrow keys
    # win.nodelay(1)  # Do not wait for keypress
    curses.curs_set(0)  # Hide cursor
    # curses.cbreak()  # Read keys instantaneously
    # curses.noecho()
    # stdscr.addstr(rows, cols, 'a')
    # stdscr.addstr(0, 0, "Current mode: Typing mode",
    #           curses.A_REVERSE)
    # stdscr.addstr("Pretty text", curses.color_pair(1))
    # stdscr.nodelay(True)
    ch = curses.getch()
    stdscr.addstr('abc')
    if ch == curses.KEY_MOUSE:
    	event = curses.getmouse()
    	print(event)
    # print(a)
    # stdscr.leaveok(False)
    
    


# wrapper(main)
if __name__ == '__main__':
	curses.start_color()
	curses.cbreak()
	# if curses.can_change_color():
	# 	exit()
	# print('a', stdscr.getmaxyx())
	curses.mousemask(curses.ALL_MOUSE_EVENTS)
	while True:
		main(stdscr)
		time.sleep(0.5)