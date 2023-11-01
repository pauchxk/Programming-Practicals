#Score: 10/10#
from graphics import *

def theBoxer():
    win = GraphWin("Stick figure", 300, 200)
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    arms = Line(Point(60, 90), Point(140, 90))
    arms.draw(win)
    leg1 = Line(Point(100, 120), Point(70, 170))
    leg1.draw(win)
    leg2 = Line(Point(100, 120), Point(130, 170))
    leg2.draw(win)

    glovecentreleft = Point(60,90)
    glovecentreright = Point(140,90)
    leftglove = Circle(glovecentreleft,10)
    leftglove.setFill("red")
    leftglove.draw(win)
    rightglove = Circle(glovecentreright,10)
    rightglove.setFill("red")
    rightglove.draw(win)

    eyecentreleft = Point(90,60)
    eyecentreright = Point(110,60)
    eyeleft = Circle(eyecentreleft,5)
    eyeright = Circle(eyecentreright,5)
    eyeleft.draw(win)
    eyeright.draw(win)

    message = Text(Point(180,30),"punch me!")
    message.draw(win)
    
    win.getMouse()
    message.setText("ow")

    owstr = 'o'

    for i in range(2,10):
        win.getMouse()
        message.setText(f"{owstr*i}w")

    win.getMouse()
    message.setText("OK, enough!")
    eyeleft.setFill("black")

    win.getMouse()

theBoxer()
