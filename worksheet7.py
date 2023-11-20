from graphics import *

def countDown():
    i = 10
    while i > 0:
        print(i, "...", end=" ")
        i = i - 1
    print("Blast Off!")


# Note: msg == "" needs to appear twice here
def getString1():
    msg = ""
    while msg == "":
        msg = input("Enter a non-empty string: ")
        if msg == "":
            print("You didn't enter anything!")
    return msg


def getString2():
    while True:
        msg = input("Enter a non-empty string: ")
        if msg != "":
            break
        print("You didn't enter anything!")
    return msg


def addUpNumbers1():
    total = 0
    more = "y"
    while more == "y":  # The loop runs while `more` is "y"
        number = int(input("Enter a number "))
        total = total + number
        more = input("Any more numbers? ")
    print("The total is", total)


def addUpNumbers2():
    total = 0
    number = int(input("Number (0 to stop): "))
    while number != 0:  # The loop runs while `number` is not 0
        total = total + number
        number = int(input("Number (0 to stop): "))
    print("The total is", total)


def addUpNumbers3():
    total = 0
    nStr = input("Number (hit enter to stop): ")
    while nStr != "":  # The loop runs while `nStr` is not empty
        number = int(nStr)  # Assumes that `nStr` contains a number
        total = total + number
        nStr = input("Number (hit enter to stop): ")
    print("The total is", total)


def addUpNumbers4():
    total = 0
    while True:  # The loop runs until we break it
        nStr = input("Number (anything else to stop): ")
        if not nStr.isdigit():
            break  # Break the loop if `nStr` is not a number
        number = int(nStr)
        total = total + number
    print("The total is", total)

# For exercise 6
def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32

#1:
def getName():
    while True:
        name = input("Enter your name: ")
        if name.isalpha() == True:
            break
        print("NUH UH")
    return name

#2:
from time import sleep
def trafficLights():
    win = GraphWin()
    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    while True:
        amber.setFill("yellow")
        sleep(3)
        green.setFill("green")
        red.setFill("black")
        amber.setFill("black")
        sleep(5)
        green.setFill("black")
        amber.setFill("yellow")
        sleep(3)
        red.setFill("red")
        amber.setFill("black")
        sleep(5)

#3:
import worksheet6
def gradeCoursework():
    mark = 30
    while mark > 20 or mark < 0:
        mark = int(input("Enter mark: "))
    print(worksheet6.calculateGrade(mark))

#4:
def orderPrice():
    ismore = 'y'
    totalcost = 0
    while ismore == 'y':
        unitprice = float(input("Enter unit price: "))
        quantity = int(input("Enter quantity of product: "))
        totalcost += unitprice * quantity
        ismore = input("Any more products? (y/n): ")
    print(totalcost)

#5:
def clickableEye():
    win = GraphWin("brown eyed GUI", 400,400)
    worksheet6.drawColouredEye(win, Point(200,200), 100, "brown")
    closewin = False
    message = Text(Point(200,350),'')
    message.draw(win)
    while closewin == False:
        pointclicked = win.getMouse()
        distancefromeye = float(worksheet6.distanceBetweenPoints(pointclicked, Point(200,200)))
        if distancefromeye < 30:
            message.setText("Pupil")
        elif distancefromeye < 50:
            message.setText("Iris")
        elif distancefromeye <= 100:
            message.setText("Sclera")
        elif distancefromeye > 100:
            closewin = True
    win.close()

#6:
def temperatureConverter():
    stop = False
    while stop == False:
        decision = int(input('f to c (1) or c to f (2) or quit (3)?: '))
        if decision == 1:
            print(f"{fahrenheit2Celsius(float(input('Enter farenheit value: '))):.2f}")
        elif decision == 2:
            print(f"{celsius2Fahrenheit(float(input('Enter celcius value: '))):.2f}")
        elif decision == 3:
            stop = True

#7:
def tableTennisScorer():
    win = GraphWin("Ping Pong",400,400)
    divider = Line(Point(200,0),Point(200,400))
    divider.draw(win)
    leftscore = Text(Point(100,200),'0')
    leftscore.draw(win)
    rightscore = Text(Point(300,200),'0')
    rightscore.draw(win)

    leftscorec = 0
    rightscorec = 0
    winner = 0
    while max(leftscorec, rightscorec) < 11 or abs(leftscorec - rightscorec) < 2:
        location = win.getMouse()
        if location.getX() < 200:
            leftscorec += 1
            leftscore.setText(leftscorec)
        if location.getX() > 200:
            rightscorec += 1
            rightscore.setText(rightscorec)
    
    if leftscorec > rightscorec:
        congrats = Text(Point(100,250),"Winner!")
        congrats.draw(win)
    elif rightscorec > leftscorec:
        congrats = Text(Point(300,250),"Winner!")
        congrats.draw(win)
    win.getMouse()
    
#8:
from random import randint
def guessTheNumber():
    numb = randint(0,100)
    for i in range(0,7):
        guess = int(input("Enter guess: "))
        if guess == numb:
            print(f"Correct! It took you {i} guesses.")
            quit()
        elif guess > numb:
            print("Too high!")
        elif guess < numb:
            print("Too low!")
    print(f"Out of guesses! The correct number was {numb}.")

#9:
def clickableBoxOfEyes(rows, columns):
    #definitions#
    padding = 50
    eye_radius = 50
    container_height = rows * 100
    container_width = columns * 100

    top_left = Point(padding, padding)
    bottom_right = Point(padding + container_width, padding + container_height)

    #opening window to appropriate size#
    win = GraphWin('eyes', container_width + padding*2, container_height + padding*2)

    #drawing container for eyes#
    container = Rectangle(top_left, bottom_right)
    container.draw(win)

    #list of eye positions#
    eye_positions = []

    #drawing eyes#
    for i in range(rows):
        for j in range(columns):

            centre_x = (top_left.getX() + (eye_radius * j)) * 2
            centre_y = (top_left.getY() + (eye_radius * i)) * 2

            eye_positions.append((centre_x, centre_y))

            worksheet6.drawColouredEye(win, Point(centre_x, centre_y), eye_radius, 'blue')

    #empty text box for click locations#
    message = Text(Point(container_width / 2 + padding, container_height + padding + 20), "")
    message.draw(win)

    #finding click locations
    while True:
        click_point = win.getMouse()
        #if click point is within container#
        if top_left.getX() < click_point.getX() < bottom_right.getX() and top_left.getY() < click_point.getY() < bottom_right.getY():
            clicked_on_eye = False

            #enumerate eye positions#
            for i, (eye_x, eye_y) in enumerate(eye_positions, start=1):
                
                #find distance between click point and the location of the current eye#
                distance = float(worksheet6.distanceBetweenPoints(click_point, Point(eye_x, eye_y)))

                #if distance is smaller than the eye radius, print location of current eye then break from loop#
                if distance <= eye_radius:
                    message.setText(f"Clicked on eye at row {((i - 1) // columns) + 1}, column {(i - 1) % columns + 1}")
                    clicked_on_eye = True
                    break
            
            #if no eye coordinate
            if clicked_on_eye == False:
                message.setText("Between eyes")

        #if click point is outside of container#
        else:
            break
    win.close()

#10:
def findTheCircle():
    win = GraphWin("FIND. THAT. CIRCLE!",600,600)
    notfound = False
    found = False
    rad = 30
    points = 0
    win.getMouse()
    message = Text(Point(300,20),'')
    message.draw(win)

    while notfound == False:

        randcoordx = randint(30,570)
        randcoordy = randint(30,570)
        circle = Circle(Point(randcoordx,randcoordy), rad)
        prevguess = Point(0,0)

        for i in range(10, -1, -1):

            found = False
            clickpoint = win.getMouse()
            distancefromcircle = float(worksheet6.distanceBetweenPoints(Point(clickpoint.getX(),clickpoint.getY()), Point(randcoordx,randcoordy)))

            if distancefromcircle <= 30:
                circle.draw(win)
                points += i
                found = True
                message.setText(f"Found it! added {i} points.")
                sleep(3)
                message.setText('')
                break

            elif distancefromcircle > 30 and prevguess != Point(0,0):
                if distancefromcircle < float(worksheet6.distanceBetweenPoints(Point(prevguess.getX(),prevguess.getY()), Point(randcoordx,randcoordy))):
                    message.setText(f"Getting closer! Attempts left: {i}")
                    prevguess = clickpoint
                elif distancefromcircle > float(worksheet6.distanceBetweenPoints(Point(prevguess.getX(),prevguess.getY()), Point(randcoordx,randcoordy))):
                    message.setText(f"Getting further away! Attempts left: {i}")
                    prevguess = clickpoint

        if found == True:
            rad *= 0.9
            i = 10

        if found == False:
            notfound = True
    
    message.setText(f"GAME OVER! Total: {points}")
    win.getMouse()
    win.close()