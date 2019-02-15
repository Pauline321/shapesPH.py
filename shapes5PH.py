#shapes5PH.py by Pauline Harrell
from graphics import*
bTriWin = GraphWin("Blue Triangle", 700, 700)
bTriWin.setCoords (90,90,900,900)

bTri = Polygon(Point(100,100),Point (150,200),Point(200,100))
bTri.setFill(color_rgb(30,30,230))
bTri.draw(bTriWin)

gCircle = Circle(Point(865,865),30.5)
gCircle.setFill(color_rgb(30,230,30))
gCircle.draw(bTriWin)




bTnWin.getMouse()
bTriWin.close()
