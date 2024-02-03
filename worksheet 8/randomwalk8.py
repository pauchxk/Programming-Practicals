from random import random
from worksheet6 import distanceBetweenPoints

def main():
    numWalks, numSteps = getInputs()
    averageSteps = takeWalks(numWalks, numSteps)
    printExpectedDistance(averageSteps)

def getInputs():
    numWalks = int(input("How many random walks to take? "))
    numSteps = int(input("How many steps for each walk? "))
    return numWalks, numSteps

def takeWalks(numWalks, numSteps):
    totalSteps = 0
    for _ in range(numWalks):
        location = takeAWalk(numSteps)
        distancefromstart = float(distanceBetweenPoints(Point(0,0),Point(location[0],location[1])))
        totalSteps += distancefromstart
    return totalSteps / numWalks

def printExpectedDistance(averageSteps):
    print(f"The expected number of steps away from the start point is {averageSteps:.2f}")

def takeAWalk(numSteps):
    stepsForwardOfStart = [0,0]
    for step in range(numSteps):
        if random() <= 0.25:
            stepsForwardOfStart[0] += 1
        elif random() <= 0.5:
            stepsForwardOfStart[0] -= 1
        elif random() <= 0.75:
            stepsForwardOfStart[1] += 1
        elif random() <= 1:
            stepsForwardOfStart[1] -= 1
    return stepsForwardOfStart

main()