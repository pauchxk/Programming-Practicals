#NOTE: FIX Y POS


import math
from graphics import *

def greet(name):
    return f"Hello, {name}!"

def product(a, b):
    return a * b

def divide(a, b):
    return a / b

def divdeAndProduct(a, b):
    productResult = product(a, b)
    divideResult = divide(a, b)
    return productResult, divideResult

def main():
    myName = input("What is your name? ")
    greeting = greet(myName)
    print(greeting)

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    productResult, divideResult = divdeAndProduct(num1, num2)
    print(f"{num1} * {num2} = {productResult}")
    print(f"{num1} / {num2} = {divideResult}")

def calcFutureValue(amount, years):
    interestRate = 0.065
    for year in range(years):
        amount = amount * (1 + interestRate)
    return amount

def futureValue():
    amount = float(input("Enter an amount to invest: "))
    years = int(input("Enter the number of years: "))
    final = calcFutureValue(amount, years)

    output = f"Investing £{amount:0.2f} for {years} years "
    output += f"results in £{final:0.2f}."
    print(output)

# For exercises 1 and 2
def areaOfCircle(radius):
    return math.pi * radius ** 2

# For exercise 3
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

#1: The pract5.py file contains a function areaOfCircle which has a parameter representing a circle’s radius, and 
#returns the area of the circle. Write a similar function called circumferenceOfCircle that has a radius parameter 
#and returns the circumference of the circle.
def circumferenceOfCircle(radius):
    return round(float(2*math.pi*radius),2)

#2: Write a function circleInfo which asks the user to input the radius of a circle, and then outputs a message that 
#includes both the area and the circumference of the circle (displayed to three decimal places). For example, if the 
#user enters a radius of 5, then the output message might be: The area is 78.540 and the circumference is 31.416
#Your function should call both areaOfCircle and circumferenceOfCircle.
def circleInfo():
    radius = float(input('Enter radius: '))
    circumference = circumferenceOfCircle(radius)
    area = areaOfCircle(radius)
    return f"The area is {area:.3f} and the circumference is {circumference:.3f}"

#3: The drawCircle function in pract5.py draws a circle on a graphics window with a given centre point, radius, and 
#colour. Complete the drawBrownEyeInCentre function in pract5.py so that it calls drawCircle three times 
#to draw a brown “eye” in the centre of a graphics window. The radii of the circles should be 60, 30 and 15.
def drawBrownEyeInCentre():
    window = GraphWin()
    drawCircle(window, Point(100,100), 60, "white")
    drawCircle(window, Point(100,100), 30, "brown")
    drawCircle(window, Point(100,100), 15, "black")
    window.getMouse()

#4: Write a function drawBlockOfStars which has two parameters, width and height and outputs a rectangle of asterisks of 
#the appropriate dimensions. Now, write a function drawLetterE that displays a large capital letter E. Your function should 
#work by calling the drawBlockOfStars function an appropriate number of times.
def drawBlockOfStars(width, height):
    for _ in range(height):
        print('*'*width)

def drawLetterE():
    drawBlockOfStars(8,2)
    drawBlockOfStars(2,2)
    drawBlockOfStars(5,2)
    drawBlockOfStars(2,2)
    drawBlockOfStars(8,2)

#5: Add code to the drawBrownEye function in the pract5.py file so 
#that, by calling drawCircle three times, it draws a single brown 
#“eye”. The graphics window, centre point and radius of the eye must 
#all be given as parameters to your drawBrownEye function.  Now, 
#using your completed drawBrownEye function, write another 
#function called drawPairOfBrownEyes (without parameters) that 
#draws a pair of eyes on a graphics window.
# For exercise 5
def drawBrownEye(win, centre, radius):
    drawCircle(win, centre, radius, 'white')
    drawCircle(win, centre, (radius/2), 'brown')
    drawCircle(win, centre, (radius/4), 'black')

def drawPairOfBrownEyes():
    win = GraphWin("",400,200)
    drawCircle(win, Point(140,100), 60, 'white')
    drawCircle(win, Point(140,100), 30, 'brown')
    drawCircle(win, Point(140,100), 15, 'black')
    drawCircle(win, Point(260,100), 60, 'white')
    drawCircle(win, Point(260,100), 30, 'brown')
    drawCircle(win, Point(260,100), 15, 'black')
    win.getMouse()

#6: Write a function distanceBetweenPoints that has two parameters 
#p1 and p2, each of type Point and returns the distance between 
#them. This function should use the Pythagoras’ Theorem 
#(see worksheet 2). For example, the function call 
#distanceBetweenPoints(Point(1, 2), Point(4, 6)) 
#should result in the value 5.0 being returned.
def distanceBetweenPoints(p1,p2):
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return f'{float(distance):.1f}'


#7: Write a function distanceCalculator that shows a graphics window 
#to the user and using a Text object asks the user to click on 
#two locations of the window. Your function should then 
#call distanceBetweenPoints from the previous question 
#and update the text of the Text object to display 
#the distance between the points.
def distanceCalculator():
    win = GraphWin()
    message = Text(Point(100,10), "Click two points :)")
    message.draw(win)
    point1 = win.getMouse()
    point2 = win.getMouse()
    distanceline = Line(point1,point2)
    distanceline.draw(win)
    distance = distanceBetweenPoints(point1, point2)
    message.setText(f"distance = {distance}")
    win.getMouse()

#8: It is impossible to output letters such as A or O using the 
#drawBlockOfStars function. To allow for more complex letters such 
#as these, write a new function drawBlocks that outputs up to four 
#rectangles next to each other (consisting of spaces, then asterisks, 
#then spaces and finally asterisks, all the same height). The widths 
#of the four rectangles and their common height should be parameters. 
#E.g., a call: drawBlocks(0, 5, 4, 3, 2). Note that there are 
#no spaces before the first asterisks due to the 0 argument. 
#Now, write a function drawLetterA that uses drawBlocks to 
#display a large capital A in asterisks.
def drawBlocks(space1, block1, space2, block2, height):
    space = ' '
    block = '*'
    for _ in range(height):
        print(f"{(space*space1)}{(block*block1)}{(space*space2)}{(block*block2)}")

def drawLetterA():
    drawBlocks(1,8,1,0,2)
    drawBlocks(0,2,6,2,2)
    drawBlocks(0,10,0,0,2)
    drawBlocks(0,2,6,2,3)

#9: Write a drawFourPairsOfBrownEyes function (which doesn’t 
#have parameters) that opens a graphics window and allows the 
#user to “draw” four pairs of eyes. Each pair is drawn by 
#clicking the mouse twice: The first click gives the centre 
#of the left-most eye, and the second gives any point on 
#the outer circumference of this eye.
def drawFourPairsOfBrownEyes():
    win = GraphWin('',1000,500)
    message = Text(Point(500,20),'Click twice')
    message.draw(win)

    for _ in range(4):
        centre = win.getMouse()
        radpoint = win.getMouse()
        radius = float(distanceBetweenPoints(centre, radpoint))

        rightcentrex_temp = centre.getX()
        rightcentrex = rightcentrex_temp + (radius*2)
        rightcentrey = centre.getY()
        rightcentre = Point(rightcentrex, rightcentrey)

        drawBrownEye(win, centre, radius)
        drawBrownEye(win, rightcentre, radius)
    win.getMouse()

#10: Harder: Write a displayTextWithSpaces function which will 
#display a given string at a given point size at a given position 
#on a given graphics window (i.e., it should have four parameters). 
#The string should be displayed with spaces between each character 
#and in uppercase. For example, “hello” should be displayed as 
#“H E L L O”. Now, using this function, write another function 
#constructVisionChart that constructs an optician’s vision 
#chart. Your function should first open a graphics window. 
#It should then ask the user for six strings, displaying them on 
#the graphics window as they are entered. The strings should be 
#displayed in upper case, and from the top of the window to the 
#bottom with descending point sizes of 30, 25, 20, 15, 10 and 5.
def displayTextWithSpaces(win, inptext, position, size):
    ndisplay = Text(position,' '.join(inptext.upper()))
    ndisplay.setSize(size)
    ndisplay.draw(win)
    win.getMouse()
    
def constructVisionChart():
    win = GraphWin("Vision Chart", 600, 400)
    counter = 100
    font = 30
    x = 50

    for _ in range(6):
        message = Text(Point(300,counter), ' '.join(input("Enter string: ")).upper())
        message.setSize(font)
        message.draw(win)

        x -= 5
        counter += x
        font -= 5

    win.getMouse()

#11: Harder: Write a drawStickFigureFamily function. This function 
#should display a group of four or five stick figures (representing 
#a family) in a graphics window. All the stick figures should be 
#the same shape (same as exercise 1, worksheet 3), but they 
#should be of different sizes and positions. Begin by copying 
#your drawStickFigure function from pract3.py, and changing 
#it so that it has three  parameters, representing a graphics 
#window, the position of the figure (a Point) and its size 
#(an int). What the position and size mean exactly is up 
#to you. Your drawStickFigureFamily function should contain 
#just four or five calls to the modified version of drawStickFigure. 
def drawStickFigure(win, position, size):
    posx = position.getX()
    posy = position.getY()
    head = Circle(Point(posx, (posy-size*2.5)), (size/2))
    head.draw(win)
    body = Line(Point(posx, (posy-size)), Point(posx, (posy-size*2)))
    body.draw(win)
    arm1 = Line(Point(posx, (posy-size*2)), Point((posx-size/1.5), (posy-size*1.5)))
    arm1.draw(win)
    arm2 = Line(Point(posx, (posy-size*2)), Point((posx+size/1.5), (posy-size*1.5)))
    arm2.draw(win)
    leg1 = Line(Point(posx, (posy-size)), Point((posx-size/2), posy))
    leg1.draw(win)
    leg2 = Line(Point(posx, (posy-size)), Point((posx+size/2), posy))
    leg2.draw(win)

def drawStickFigureFamily():
    win = GraphWin("Stick Figure Family", 600, 400)
    drawStickFigure(win, Point(100,350), 80)
    drawStickFigure(win, Point(200,350), 60)
    drawStickFigure(win, Point(300,350), 40)
    drawStickFigure(win, Point(400,350), 50)
    drawStickFigure(win, Point(500,350), 90)
    win.getMouse()

drawStickFigureFamily()