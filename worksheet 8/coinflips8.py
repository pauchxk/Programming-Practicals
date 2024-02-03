from random import randint
import math

def main():
    flipsnum = getInputs()
    x, y = simulateFlips(flipsnum)
    headsprop = float(x / flipsnum)
    tailsprop = float(y / flipsnum)
    displayResults(headsprop, tailsprop)

def getInputs():
    flipsnum = int(input("Enter amount of times to flip coin: "))
    return flipsnum

def simulateFlips(flipsnum):
    headstotal = 0
    tailstotal = 0
    for _ in range(flipsnum):
        headortail = randint(1,2)
        if headortail == 1:
            headstotal += 1
        elif headortail == 2:
            tailstotal += 1
    return headstotal, tailstotal

def displayResults(headsprop, tailsprop):
    print(f"Heads {headsprop}\nTails {tailsprop}")

main()