from math import *
#1: Write a function speedCalculator that asks the user for two integers: 
#the distance travelled in km (kilometres) and the duration of the journey in hours. 
#speedCalculator should then output the speed in kilometres per hour (km/h). 
def speedCalculator():
    distance = int(input('Enter distance in km: '))
    duration = int(input('Enter duration in hrs: '))
    print('Speed =',distance/duration)

#2: Write a function circumferenceOfCircle that asks the user for the radius of a 
#circle. The function should then output (print) the circle’s circumference. 
def circumferenceOfCircle():
    radius = int(input('Enter radius: '))
    circumference = 2*pi*radius
    print(circumference)

#3: Write a function areaOfCircle that asks the user for the radius of a circle. 
#It should then output the circle’s area.
def areaOfCircle():
    radius = int(input('Enter radius: '))
    area = pi*radius**2
    print(area)

#4: Write a function costOfPizza that asks the user for the diameter of a pizza (in cm) 
#your function should then output the cost of the pizza (based on its area) in pounds. 
#Assume that the cost of the ingredients is 3.5 pence per square cm.
def costOfPizza():
    diameter = int(input('Enter diameter: '))
    radius = diameter/2
    area = pi*radius**2
    cost = area * 3.5
    cost /= 100
    print('Pizza cost: $'+cost)

#5: Write a function slopeOfLine that first asks the user for four values 
#x1, y1, x2 and y2 that represent two points in two-dimensional space 
#(i.e. points with coordinates (x1, y1) and (x2, y2)). The function should then 
#output the slope of the line that connects them.
def slopeOfLine():
    x1 = float(input('Enter x value 1: '))
    y1 = float(input('Enter y value 1: '))
    x2 = float(input('Enter x value 2: '))
    y2 = float(input('Enter y value 2: '))
    if x1 == x2:
        print('The slope is undefined (vertical line).')
    elif y1 == y2:
        print('The slope is undefined (horizontal line).')
    else:
        slope = (y2-y1)/(x2-x1)
        print(f'The slope of the line through ({x1},{y1}) and ({x2},{y2}) is {slope}')

#6: Write a function distanceBetweenPoints that asks the user for four values 
#x1, y1, x2 and y2 that represent two points in two-dimensional space, and 
#then outputs the distance between them.
def distanceBetweenPoints():
    x1 = float(input('Enter x value 1: '))
    y1 = float(input('Enter y value 1: '))
    x2 = float(input('Enter x value 2: '))
    y2 = float(input('Enter y value 2: '))
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f'The distance between the two points ({x1},{y1}) and ({x2},{y2}) is {distance}')

#7: Write a function travelStatistics which asks the user to input the average 
#speed (in km/hour) and duration (in hours) of a car journey. The function should then 
#output the overall distance travelled (in km), and the amount of fuel used (in litres) 
#assuming a fuel efficiency of 5 km/litre.
def travelStatistics():
    avg_speed = int(input('Enter average speed (km/h): '))
    duration = int(input('Enter duration (hrs): '))
    distance_travelled = avg_speed * duration
    fuel_used = distance_travelled / 5
    print(f'Distance travelled was {distance_travelled}km, using {fuel_used}litres of fuel.')

#8: Write a function sumOfSquares that uses a loop to output the sum 1^2 + 2^2 + … + n^2 
#where n is an integer provided by the user.  For example, if the user enters 
#3, the function should output 14 (1^2 + 2^2 + 3^2).
def sumOfSquares():
    n = int(input('Enter value: '))
    squaresum = 0
    for vals in range(1, n):
        squaresum += (vals**2)
    print(squaresum)

#9: Write a function averageOfNumbers which outputs the average of a series of numbers 
#entered by the user. The function should first ask the user how many 
#numbers there are to be inputted.
def averageOfNumbers():
    amount = int(input('Enter amount of numbers: '))
    total = 0
    for count in range(amount):
        total += int(input('Enter value: '))
    average = total / count

#10: Harder: Write a function fibonacci which asks the user for a 
#number n. Use a loop to calculate and output the nth value in the Fibonacci sequence.
def fibonacci():
    n = int(input('Enter value: '))
    cur = 1
    old = 1
    i = 1
    for i in range(n-2):
        cur, old = cur+old, cur
    print(cur)

#11: Harder: Write a function selectCoins that asks the user an amount of money 
#in pence. It should output the number of coins of each denomination (£2 to 1p) 
#that should be used to make up that amount.  
def selectCoins():
    amount_in_pence = int(input('Enter amount in pence: '))
    denominations = {
        '$2': 200,
        '$1': 100,
        '50p': 50,
        '20p': 20,
        '10p': 10,
        '5p': 5,
        '2p': 2,
        '1p': 1
    }
    coins_count = {denomination: 0 for denomination in denominations}
    for denomination, value in denominations.items():
        if amount_in_pence >= value:
            coins_count[denomination] = amount_in_pence // value
            amount_in_pence %= value
    for denomination, count in coins_count.items():
        print(f'{count} x {denomination}')
