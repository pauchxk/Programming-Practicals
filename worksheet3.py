#1: Write a function called sayName that displays your name. 
def sayName():
    print('James')

#2: Write a sayHello2 function that uses two print statements to display the text below:
def sayHello2():
    print('Hello')
    print('World')

#3: Write a function called dollars2Pounds which converts a dollar's value to pounds.
def dollars2Pounds():
    dollars = int(input('Enter value in dollars: '))
    pounds = 0.8 * dollars
    print(pounds)

#4: Write a tenHellos function that uses a loop to display “Hello World” ten times (on separate lines). 
def tenHellos():
    for i in range(10):
        print('Hello World')
        
#5: Suppose the prices of train tickets are increasing by 2% every month. Write a function called
#railFareIncrease which begins by printing the current price of a ticket from Southampton to
#Portsmouth: £16.50. It should then display the price for 11 more months.
def railFareIncrease():
    current_price = 16.50
    for i in range(11):
        current_price *= 1.02
        print(current_price)

#6: Write a countTo function that asks the user for a number and then counts from 1 to that number.
def countTo():
    n = int(input('Enter a number: '))
    for i in range(1,n+1):
        print(i)
        
#7: Based on your solution to the previous question, write a function called countFromTo that asks
#the user for two numbers. The first number is the start of the count and the second one is where the count ends.
def countFromTo():
    x = int(input('Enter a number: '))
    y = int(input('Enter another number: '))
    for i in range(x,y+1):
        print(i)
        
#8: Write a changeCounter function. This should ask the user how many 1p, 2p and 5p coins they have
#(using separate questions), and then display the total amount of money in pence.
def changeCounter():
    p1 = int(input('Enter 1p: '))
    p2 = int(input('Enter 2p: '))
    p5 = int(input('Enter 5p: '))
    total = p1 + (p2*2) + (p5*5)
    print(total)
    
#9: Harder: Write a function weightsTable that prints a table of kilogram weights
#(between 10 and 50) and their ounce equivalents. The kilogram values should be displayed as shown below:
def weightsTable():
    print('KGs|Oz')
    for i in range(10,60,10):
        print(i, i*35.274)
        
#10: Harder: Write a function called futureRailFare that uses a for loop to calculate the future value
#of a train ticket assuming a monthly price rise of 2%. futureRailFare needs to get two values from
#the user (the initial fare and the number of months).
def futureRailFare():
    fare = float(input('Enter initial fare: '))
    months = int(input('Enter no. of months: '))
    for i in range(months):
        fare *= 1.02
    print(fare)
