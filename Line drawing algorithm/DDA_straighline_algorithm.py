# Algorithm to draw a straight line using DDA algorithm
from graphics import *
import time
import ctypes
user32 = ctypes.windll.user32
scrnWidth, scrnHeight= (user32.GetSystemMetrics(0)-100), (user32.GetSystemMetrics(1)-100)

print("Straight line drawing using DDA algorithm : ")

start = tuple(int(x.strip()) for x in input("Enter starting co-ordinate of the straight line (x,y) : ").split(','))

end = tuple(int(x.strip()) for x in input("Enter ending co-ordinate of the straight line (x,y) : ").split(','))

win = GraphWin('Straight Line DDA', scrnWidth, scrnHeight)

# for drawing the axis:
xAxis = Line(Point(0,int(scrnHeight/2)), Point(scrnWidth, int(scrnHeight/2)))
xAxis.draw(win)
yAxis = Line(Point(int(scrnWidth/2),0), Point(int(scrnWidth/2), scrnHeight))
yAxis.draw(win)

# for printing the message
message = Text(Point(win.getWidth()/2, 30), 'Straight line drawing using DDA algorithm : ')
message.setTextColor('red')
message.setStyle('italic')
message.setSize(20)
message.draw(win)

message = Text(Point(win.getWidth()/2, win.getHeight()-20), 'Click on the window to close')
message.setTextColor('red')
message.setStyle('italic')
message.setSize(20)
message.draw(win)


# DDA algorithm
x1,y1 = start
x2,y2 = end


dx = x2 - x1
dy = y2 - y1

if (abs(dx) >= abs(dy)):
    L = abs(x2-x1)
else:
    L = abs(y2-y1)

# calculate increment factor
delta_x = (x2 - x1)/L
delta_y = (y2 - y1)/L

x_new = x1 + 0.5
y_new = y1 + 0.5

pt = Point(int(x_new), int(y_new))
pt.draw(win)

i = 1

while(i <= L):
    time.sleep(0.1)
    x_new += delta_x
    y_new += delta_y
    pt = Point(int(x_new), int(y_new))
    pt.draw(win)
    i += 1
    
win.getMouse()
win.close()
