#shapes5PH.py by Pauline Harrell
from graphics import*

bTriWin = GraphWin("Blue Triangle", 700, 700)
bTriWin.setCoords (0,0,700,700)

bTri = Polygon(Point(20,25),Point (70,120),Point(110,25))
bTri.setFill(color_rgb(30,30,230))
bTri.draw(bTriWin)

gCircle = Circle(Point(665,665),30)
gCircle.setFill(color_rgb(30,230,30))
gCircle.draw(bTriWin)

pRectangle = Rectangle(Point(460,100),Point (680,15))
pRectangle.setFill(color_rgb(100,0,150))
pRectangle.draw(bTriWin)

pRectangle = Rectangle(Point(100,400),Point (15,400))
pRectangle.setFill(color_rgb(600,0,200))
pRectangle.draw(bTriWin)



bTriWin.getMouse()

bTriWin.close()
