# Ellipse drawing algorithm
from graphics import *
import time
import ctypes
user32 = ctypes.windll.user32
scrnWidth, scrnHeight= (user32.GetSystemMetrics(0)-100), (user32.GetSystemMetrics(1)-100)
print("Ellipse drawing algorithm : ")

a,b = tuple(int(x.strip()) for x in input("Enter major & minor axis of the Ellipse (a,b) : ").split(','))
center = tuple(int(x.strip()) for x in input("Enter co-ordinate of the center of the Ellipse (x,y) : ").split(','))

# configuring the window
win = GraphWin('Circle Drawing using Midpoint Algorithm', scrnWidth, scrnHeight)

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

message = Text(Point(win.getWidth()/2, 30), 'Ellipse drawing algorithm Algorithm')
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


def plotEllipse(xNew,yNew):
    # uses 4 point symmetry to plot 4 points using only one point calculation 
    pt = Point(xCenter+xNew, yCenter+yNew)
    pt.draw(win)
    pt = Point(xCenter-xNew, yCenter+yNew)
    pt.draw(win)
    pt = Point(xCenter+xNew, yCenter-yNew)
    pt.draw(win)
    pt = Point(xCenter-xNew, yCenter-yNew)
    pt.draw(win)

# plot center point
pt = Point(xCenter, yCenter)
pt.draw(win)

# Ellipse drawing algorithm:
    
x = 0
y = b
fx = 0
fy = 2 * a**2 * b
p = int(b**2 - a**2 * b + 0.25 * a**2) # decision parameter

#compute next pixel

while(fx < fy): # steps for drawing portion where fx<fy i.e. starting from y axis
    time.sleep(0.01) # delay generation to visualize each step
    plotEllipse(x,y)
    x += 1
    fx = fx + 2 * b**2
    if(p<0):
        p = p + fx + b**2
    else:
        y -= 1
        fy = fy - 2 * a**2
        p = p + fx + b**2 - fy
plotEllipse(x,y)


p = int( b**2 * (x+0.5)**2 + a**2 * (y-1)**2 - a**2 * b**2) # decision parameter

while(y>0): # steps for drawing portion where x=y to y=0 i.e. starting from x axis
    time.sleep(0.01) # delay generation to visualize each step
    y -= 1
    fy = fy - 2 * a**2
    if(p >= 0):
        p = p - fy + a**2
    else:
        x += 1
        fx = fx + 2 * b**2
        p = p + fx - fy + a**2
    plotEllipse(x,y)
plotEllipse(x,y)

# To close the graphics window on click
win.getMouse()
win.close()


    
