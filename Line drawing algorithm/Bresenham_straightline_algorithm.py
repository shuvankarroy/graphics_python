# Algorithm to draw a straight line using Bresenham's algorithm
# works only foor lines having inclination <= 45 degree
from graphics import *
import time
import ctypes
user32 = ctypes.windll.user32
scrnWidth, scrnHeight= (user32.GetSystemMetrics(0)-100), (user32.GetSystemMetrics(1)-100)

print("Straight line drawing using Bresenham's algorithm : ")

start = tuple(int(x.strip()) for x in input("Enter starting co-ordinate of the straight line (x,y) : ").split(','))
end = tuple(int(x.strip()) for x in input("Enter starting co-ordinate of the straight line (x,y) : ").split(','))

win = GraphWin('Bresenham\'s Straight Line', scrnWidth, scrnHeight)

# for printing the message
message = Text(Point(win.getWidth()/2, 30), 'Straight line drawing using Bresenham\'s algorithm : ')
message.setTextColor('red')
message.setStyle('italic')
message.setSize(20)
message.draw(win)

message = Text(Point(win.getWidth()/2, win.getHeight()-20), 'Click on the window to close')
message.setTextColor('red')
message.setStyle('italic')
message.setSize(20)
message.draw(win)

x1,y1 = start
x2,y2 = end

pt = Point(x1,y1)
x_new,y_new = x1,y1
pt.draw(win)

delta_x = abs(x2 - x1)
delta_y = abs(y2 - y1)
p = 2 * delta_y - delta_x
i = 1

while(i <= delta_x):
    time.sleep(0.1)
    if(p < 0):
        x_new += 1
        pt = Point(x_new,y_new)
        pt.draw(win)
        p += 2*delta_y
    else:
        x_new += 1
        y_new += 1
        pt = Point(x_new,y_new)
        pt.draw(win)
        p = p + 2*delta_y - 2*delta_x
    i+=1


win.getMouse()
win.close()
