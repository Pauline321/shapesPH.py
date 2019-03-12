#shapes5PH.py by Pauline Harrell
from graphics import*

winX = 700
winY = 700
diaSz = 50

bTriWin = GraphWin("Blue Triangle", winX, winY)
bTriWin.setCoords (0,0,winX,winY)

bTri = Polygon(Point(20,25),Point (70,120),Point(110,25))
bTri.setFill(color_rgb(30,30,230))
bTri.draw(bTriWin)

gCircle = Circle(Point(665,665),30)
gCircle.setFill(color_rgb(30,230,30))
gCircle.draw(bTriWin)

pRectangle = Rectangle(Point(460,100),Point (680,15))
pRectangle.setFill(color_rgb(100,0,150))
pRectangle.draw(bTriWin)

rOval = Oval(Point(20,575), Point(220,675))
rOval.setFill(color_rgb(255,10,10))
rOval.draw(bTriWin)

tDia = Polygon(Point( winX/2 - diaSz, winY/2),
               Point(winX/2, winY/2 + diaSz),
               Point( winX/2 + diaSz ,winY/2),
               Point(winX/2, winY/2 - diaSz))
tDia.setFill(color_rgb(0,250,150))
tDia.draw(bTriWin)

bTriWin.getMouse()
bTriWin.close()
