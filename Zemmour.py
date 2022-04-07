from ti_graphics import drawImage
from ti_system import *

n = 1
for i in range(1,4):
	disp_clr()
	drawImage("Photo" + str(n), 0, 30)
	n = n+1
	wait_key()
disp_wait()

