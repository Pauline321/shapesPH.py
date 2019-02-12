#shapes5PH.py by Pauline Harrell
from graphics import*
bTriWin = GraphWin("Blue Triangle", 300, 300)
bTriWin.setCoords (0,0,300,300)

bTri = Polygon(Point(100,100),Point (150,200),Point(200,100))
bTri.setFill(color_rgb(30,30,230))
bTri.draw(bTriWin)

bTnWin.getMouse()
bTriWin.close()
