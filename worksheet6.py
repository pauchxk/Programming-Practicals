from graphics import *
import math


def greet(name):
    print("Hello", name + ".")
    if len(name) > 20:
        print("That's a long name!")


def canYouVote(age):
    if age >= 18:
        print("You can vote")
    else:
        print("Sorry, you can't vote")


def getDegreeClass(mark):
    if mark >= 70:
        return "1st"
    elif mark >= 60:
        return "2:1"
    elif mark >= 50:
        return "2:2"
    elif mark >= 40:
        return "3rd"
    else:
        return "Fail"


# We will simplify this function later in the term
def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def daysInMonth(month, year):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
        return 31


def overlyComplexDaysInMonth(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or \
       month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif isLeapYear(year):
        return 29
    else:
        return 28


def countDown():
    for i in range(10, 0, -1):
        print(i, "...", end=" ")
    print("Blast Off!")


def numberedTriangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# For exercises 8 & 11
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


#1: A fast-food company charges £2.50 for delivery to your home, except for large orders 
#of £20 or more where delivery is free. Write a function fastFoodOrderPrice that asks 
#the user for the basic price of an order and prints a “The total price of your order 
#is …” message containing the total price including any delivery charges. 
#(Try to avoid using an else clause in your solution.)
def fastFoodOrderPrice():
    price = float(input("Enter price: "))
    if price >= 20:
        print(f"The total price of your order is {price}")
    elif price < 20:
        price += 2.5
        print(print(f"The total price of your order is {price}"))

#2:
def whatToDoToday():
    temperature = float(input("Enter today's temperature: "))
    if temperature > 25:
        print("Go swim in the sea!")
    elif temperature >= 10 and temperature <= 25:
        print("Go shopping at Gunwharf!")
    elif temperature < 10:
        print('Stay home, watch a film.')

#3:
def displaySquareRoots(start, end):
    for count in range(start, end+1):
        print(f"The square root of {count} is {math.sqrt(count):.3f}")

#4:
def calculateGrade(mark):
    if mark > 20 or mark <= 0:
        return 'X'
    elif mark >= 16:
        return 'A'
    elif mark >= 12:
        return 'B'
    elif mark >= 8:
        return 'C'
    elif mark < 8:
        return 'F'

#5:
def peasInAPod():
    numofpeas = int(input("How many peas? "))
    win = GraphWin("peas'd to meet you", numofpeas*100,100)
    count = 50
    for _ in range(numofpeas):
        pea = Circle(Point(count,50),50)
        pea.setFill("green")
        pea.draw(win)
        count += 100
    win.getMouse()

#6:
def ticketPrice(distance, age):
    cost = 10.00
    kmcost = 0.15
    cost += (kmcost*distance)
    if age >= 60 or age <= 15:
        cost *= 0.6
        return f"${cost:.2f}"
    else:
        return f"${cost:.2f}"

#7:
def numberedSquare(n):
    for i in range(n, 0, -1):
        for j in range(n):
            print(i+j, end=' ')
        print()

#8:
def drawColouredEye(win, centre, radius, colour):
    drawCircle(win, centre, radius, 'white')
    drawCircle(win, centre, (radius/2), colour)
    drawCircle(win, centre, (radius/4), 'black')
    win.getMouse()

def eyePicker():
    win = GraphWin('eyes',400,400)
    centrex = int(input('Enter x: '))
    centrey = int(input('Enter y: '))
    radius = int(input('Enter radius: '))
    colour = input('Enter colour: ')
    if centrex < 400 and centrey < 400 and centrex > 0 and centrey > 0:
        drawColouredEye(win, Point(centrex, centrey), radius, colour)

#9:
def drawPatchWindow():
    win = GraphWin('patch',200,200)
    x1 = 90
    y1 = 10
    x2 = 80
    y2 = 20
    for _ in range(0,5):
        reccy = Rectangle(Point(0,y2),Point(x1,y1))
        reccy.setFill('red')
        reccy.setOutline('red')
        reccy.draw(win)
        
        reccy2 = Rectangle(Point(x2,100),Point(x1,y1))
        reccy2.setFill('red')
        reccy2.setOutline('red')
        reccy2.draw(win)

        x1 -= 20
        y1 += 20
        x2 -= 20
        y2 += 20

    win.getMouse()

#10:
def drawPatch(win, x, y, colour):
    x1 = x + 90
    y1 = y + 10
    x2 = x + 80
    y2 = y + 20
    for _ in range(0,5):
        reccy = Rectangle(Point(x,y2),Point(x1,y1))
        reccy.setFill(colour)
        reccy.setOutline(colour)
        reccy.draw(win)

        reccy2 = Rectangle(Point(x2,y+100),Point(x1,y1))
        reccy2.setFill(colour)
        reccy2.setOutline(colour)
        reccy2.draw(win)

        x1 -= 20
        y1 += 20
        x2 -= 20
        y2 += 20

#11:
def drawPatchWork():
    win = GraphWin('Patchwork',300,200)
    for i in range(0,6):
        if i >= 3:
            drawPatch(win, (i-3)*100,100,'blue')
        else:
            drawPatch(win, i*100,0,'blue')

#12:
from random import randint
from worksheet5 import distanceBetweenPoints
def archeryGame():
    win = GraphWin('Archery',400,400)
    drawCircle(win, Point(200,200), 90, 'blue')
    drawCircle(win, Point(200,200), 60, 'red')
    drawCircle(win, Point(200,200), 30, 'yellow')
    totalpoints = 0

    for _ in range(0,5):
        atmosx = randint(0,50)
        atmosy = randint(0,50)
        posorneg = randint(1,2)

        aim = win.getMouse()
        aimx = aim.getX()
        aimy = aim.getY()
        if posorneg == 1:
            truearrowx = aimx - atmosx
            truearrowy = aimy - atmosy
        if posorneg == 2:
            truearrowx = aimx + atmosx
            truearrowy = aimy - atmosy

        arrow = Circle(Point(truearrowx,truearrowy),10)
        arrow.setFill('black')
        arrow.draw(win)

        distfrombullseye = float(distanceBetweenPoints(Point(200,200),Point(truearrowx,truearrowy)))
        if distfrombullseye <= 30:
            totalpoints += 10
            print('BULLSEYE! 10 points!')
        elif distfrombullseye <= 60:
            totalpoints += 5
            print('5 points!')
        elif distfrombullseye <= 90:
            totalpoints += 2
            print('2 points :(')
    print(f"Your total is {totalpoints} points.")