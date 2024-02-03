from graphics import *
from time import sleep
from worksheet6 import distanceBetweenPoints
from random import random

def main():
    distance, numofwalks = getInputs()
    win = GraphWin("Simulated Walks", distance*2, distance*2)
    graphicsSetup(distance, win)
    walksLoop(numofwalks, distance, win)

def getInputs():
    distance = int(input("Enter distance to end walks at: "))
    numofwalks = int(input("Enter number of walks to simulate: "))
    return distance, numofwalks

def graphicsSetup(distance, win):
    outercircle = Circle(Point(distance,distance), distance)
    outercircle.draw(win)
    centrepoint = Circle(Point(distance, distance), 2)
    centrepoint.setFill('black')
    centrepoint.draw(win)
    win.getMouse()

def walksLoop(numofwalks, distance, win):
    for _ in range(numofwalks):
        takeWalk(distance, win)

def takeWalk(distance, win):
    curx = distance
    cury = distance
    prevx = distance
    prevy = distance
    while float(distanceBetweenPoints(Point(curx, cury), Point(distance, distance))) < distance:
        rand = random()
        if rand <= 0.25:
            curx = prevx + 5
            step = Line(Point(prevx,prevy), Point(curx, cury))
            step.setFill('red')
            step.draw(win)
        elif rand <= 0.5:
            curx = prevx -5
            step = Line(Point(prevx,prevy), Point(curx, cury))
            step.setFill('blue')
            step.draw(win)
        elif rand <= 0.75:
            cury = prevy + 5
            step = Line(Point(prevx,prevy), Point(curx, cury))
            step.draw(win)
            step.setFill('green')
        elif rand <= 1:
            cury = prevy - 5
            step = Line(Point(prevx,prevy), Point(curx, cury))
            step.setFill('black')
            step.draw(win)

        prevx = curx
        prevy = cury
main()