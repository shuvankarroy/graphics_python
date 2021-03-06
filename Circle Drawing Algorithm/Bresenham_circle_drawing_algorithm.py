# Bresenham's circle drawing algorithm
from graphics import *
import time
import ctypes
user32 = ctypes.windll.user32
scrnWidth, scrnHeight= (user32.GetSystemMetrics(0)-100), (user32.GetSystemMetrics(1)-100)

print("Circle drawing using Bresenham's algorithm : ")

center = tuple(int(x.strip()) for x in input("Enter co-ordinate of the center of the circle (x,y) : ").split(','))
radius = int(input("Enter radius of the circle : "))

# configuring the window
win = GraphWin('Circle drawing using Bresenham\'s algorithm', scrnWidth, scrnHeight)

# for drawing the axis:
xAxis = Line(Point(0,int(scrnHeight/2)), Point(scrnWidth, int(scrnHeight/2)))
xAxis.draw(win)
yAxis = Line(Point(int(scrnWidth/2),0), Point(int(scrnWidth/2), scrnHeight))
yAxis.draw(win)

# for marking out the axis :
xPoint = Text(Point(win.getWidth() - 30, win.getHeight()/2 + 10), '+ X axis')
xPoint.draw(win)
xPoint = Text(Point(30, win.getHeight()/2 + 10), '- X axis')
xPoint.draw(win)

yPoint = Text(Point(win.getWidth()/2 + 30 , 10), '+ Y axis')
yPoint.draw(win)
yPoint = Text(Point(win.getWidth()/2 + 30, win.getHeight() - 10), '- Y axis')
yPoint.draw(win)
# for printing the message
centerPoint = Text(Point(win.getWidth()/2 + 15, win.getHeight()/2 + 10), '(0,0)')
centerPoint.draw(win)

message = Text(Point(win.getWidth()/2, 30), 'Circle drawing using Bresenham\'s algorithm')
message.setTextColor('red')
message.setStyle('italic')
message.setSize(20)
message.draw(win)

message = Text(Point(win.getWidth()/2, win.getHeight()-40), 'Click on the window to close')
message.setTextColor('red')
message.setStyle('italic')
message.setSize(20)
message.draw(win)



# genereating axis based center point
xOffset = scrnWidth/2
yOffset = scrnHeight/2

xCenter, yCenter = center

if(xCenter>=0 and yCenter>=0):
    xCenter = xCenter + xOffset
    yCenter = yOffset - yCenter

elif(xCenter<=0 and yCenter>=0):
    xCenter = xOffset - abs(xCenter)
    yCenter = yOffset - yCenter

elif(xCenter<=0 and yCenter<=0):
    xCenter = xOffset + xCenter
    yCenter = yOffset + abs(yCenter)

else:
    xCenter = xOffset + abs(xCenter)
    yCenter = yOffset + abs(yCenter)


def plotCircle(xNew,yNew):
    # uses 8 point symmetry to plot 8 points using only one point calculation 
    pt = Point(xCenter+xNew, yCenter+yNew)
    pt.draw(win)
    pt = Point(xCenter-xNew, yCenter+yNew)
    pt.draw(win)
    pt = Point(xCenter+xNew, yCenter-yNew)
    pt.draw(win)
    pt = Point(xCenter-xNew, yCenter-yNew)
    pt.draw(win)
    
    pt = Point(xCenter+yNew, yCenter+xNew)
    pt.draw(win)
    pt = Point(xCenter-yNew, yCenter+xNew)
    pt.draw(win)
    pt = Point(xCenter+yNew, yCenter-xNew)
    pt.draw(win)
    pt = Point(xCenter-yNew, yCenter-xNew)
    pt.draw(win)

# plot center point
pt = Point(xCenter, yCenter)
pt.draw(win)

# Circle drawing using Bresenham's algorithm :
delta = 3 - 2*radius
x = 0
y = radius

#compute next pixel
while(x <= y):
    time.sleep(0.2) # delay generation to visualize each step
    plotCircle(x,y)
    if(delta < 0):
        delta = delta + 4*x +6
    else:
        delta = delta + 4*(x-y) + 10
        y = y-1
    x = x+1
    
# close graphics window using mouse click
win.getMouse()
win.close()
