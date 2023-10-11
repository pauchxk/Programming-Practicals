from graphics import *

def sticky():

    #create graphics window and initialise points list
    win = GraphWin("beware of anatomically incorrect stick figures gaining sentience.", 1000, 1000)
    points = []

    #embedded funtion to capture mouse clicks and append them to points
    def getMouseClick():
        p = win.getMouse()
        points.append(p)
        return p

    #create head
    p1 = getMouseClick()
    p2 = getMouseClick()
    radius = ((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2) ** 0.5 #radius/distance between two points = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    head = Circle(p1, radius)
    head.draw(win)

    #create body
    p3 = getMouseClick()
    body = Line(Point(p1.getX(), p1.getY() + radius), p3) #use (p1(y) + radius) as y co-ords to get to neck area
    body.draw(win)

    #create left arm
    p4 = getMouseClick()
    left_arm = Line(Point(p4.getX(), p4.getY()), Point(p1.getX(), p1.getY() + radius))
    left_arm.draw(win)

    #create right arm
    p5 = getMouseClick()
    right_arm = Line(Point(p5.getX(), p5.getY()), Point(p1.getX(), p1.getY() + radius))
    right_arm.draw(win)

    #create left leg
    p6 = getMouseClick()
    left_leg = Line(p3, p6)
    left_leg.draw(win)

    #create right leg
    p7 = getMouseClick()
    right_leg = Line(p3, p7)
    right_leg.draw(win)

    #wait for mouse click to close
    win.mainloop()

sticky()
