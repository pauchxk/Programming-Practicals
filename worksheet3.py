from graphics import *

#1: The drawStickFigure function in the pract3.py file is incomplete. Finish it by drawing the arms and legs.
def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    arm1 = Line(Point(100,100), Point(50,120))
    arm1.draw(win)
    arm2 = Line(Point(100,100), Point(150,120))
    arm2.draw(win)
    leg1 = Line(Point(100,120), Point(70,150))
    leg1.draw(win)
    leg2 = Line(Point(100,120), Point(130,150))
    leg2.draw(win)
    
#2: Write a drawCircle function which asks the user for the radius of a circle and then draws the circle
#in the centre of a graphics window.
def drawCircle():
    win = GraphWin('Circle')
    radius = int(input('Enter radius: '))
    centre = Point(100,100)
    circle = Circle(centre,radius)
    circle.draw(win)
    
#3: Write a drawArcheryTarget function that draws a target made of yellow, red, and blue circles.
#The sizes of the circles should be in correct proportion – i.e. the red circle should have a radius
#twice that of the yellow circle, and the blue circle should have a radius three times that of the yellow circle.
def drawArcheryTarget():
    win = GraphWin('Target Practice',750,750)
    rad = 100
    centre = Point(375,375)
    circle1 = Circle(centre,rad)
    circle1.setFill('yellow')
    circle2 = Circle(centre,(rad*2))
    circle2.setFill('red')
    circle3 = Circle(centre,(rad*3))
    circle3.setFill('blue')
    circle3.draw(win)
    circle2.draw(win)
    circle1.draw(win)

#4: Write a drawRectangle function which asks the user for the height and width of a rectangle first.
#Your function should draw the rectangle in the centre of a graphics window of size 200 × 200.
#There should be equal spaces to the left and right, and above and below the rectangle.
#Assume that the user enters values less than 200. 
def drawRectangle():
    win = GraphWin('Rectangle')
    height = int(input('Enter height: '))
    width = int(input('Enter width: '))
    centre = Point(100,100)
    x1 = (200 - width)/2
    y1 = (200 - height)/2
    x2 = x1 + width
    y2 = y1 + height
    rectangle = Rectangle(Point(x1,y1),Point(x2,y2))
    rectangle.draw(win)
    
#5: Write a blueCircle function that allows the user to draw a blue circle of radius 50 by clicking
#on the location of the circle’s centre.
def blueCircle():
    win = GraphWin('CirCOOL')
    p = win.getMouse()
    x = p.getX()
    y = p.getY()
    centre = Point(x,y)
    radius = 50
    circle = Circle(centre,radius)
    circle.setFill('blue')
    circle.draw(win)
    
#6: The function drawLine in the pract3.py file allows the user to draw a line by choosing
#two points. Notice how we use the getMouse function to get the Point from the user. 
#Write a function tenLines that allows the user to draw 10 such lines.
def tenLines():
    win = GraphWin('Draw that line',500,500)
    for i in range(10):
        message = Text(Point(100,50),'Click on first point.')
        message.draw(win)
        p1 = win.getMouse()
        message.setText('Click on second point.')
        p2 = win.getMouse()
        line = Line(p1,p2)
        line.draw(win)
        message.setText(' ')
        

#7: Write a tenStrings function which allows the user to plot 10 strings
#of their choice at locations of a graphics window chosen by clicking
#on the mouse (the strings should be entered one-by-one by the user
#within a text entry box at the top of the graphics window, clicking
#the mouse after entering each one).
def tenStrings():
    win = GraphWin('ten of em',400,400)
    strings = []
    entry_box = Entry(Point(200,20),20)
    entry_box.draw(win)
    for i in range(10):
        click_point = win.getMouse()
        string_text = entry_box.getText()
        string = Text(click_point,string_text)
        string.draw(win)
        strings.append(string)
        entry_box.setText('')
        
#8: Write a tenColouredRectangles function to allow the user to draw 10
#coloured rectangles on the screen. The user should pick the coordinates
#of the top-left and bottom-right corners of every rectangle by
#clicking on the window. The user needs to select the colour of
#each rectangle by entering a colour, for example blue, in a
#provided entry box at the top of the window. (The colour of
#each rectangle is given by the string that is in this box
#when the user clicks its bottom-right point.) The entry box
#should initially contain the string "blue". Assume that the
#user never enters an invalid colour into the entry box.
def tenColouredRectangles():
    win = GraphWin('I LOVE RECTANGLES',400,400)
    rectangles = []
    colour_entry = Entry(Point(200,20),10)
    colour_entry.setText('blue')
    colour_entry.draw(win)
    for i in range(10):
        p1 = win.getMouse()
        p2 = win.getMouse()
        colour = colour_entry.getText()
        rect = Rectangle(p1,p2)
        rect.setFill(colour)
        rect.draw(win)
        rectangles.append(rect)
        
#9: Harder: Write a fiveClickStickFigure function that allows the
#user to draw a (symmetric) stick figure in a graphics window using
#five clicks of the mouse to determine the positions of its features,
#as illustrated in the figure below. Each feature should be drawn
#as the user clicks the points.
###note: i'm not doing it as 5 clicks, or as symmetrical. purely because it's more fun this way
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