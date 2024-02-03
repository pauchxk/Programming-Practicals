from graphics import *


class MyPoint:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        output = f"MyPoint({self.x}, {self.y})"
        return output


class Square():

    def __init__(self, p1, side):
        self.p1 = p1
        self.side = side
        self.p2 = MyPoint(p1.getX() + side, p1.getY() + side)
        self.fillColour = "black"
        self.outlineColour = "black"

    def getP1(self):
        return self.p1

    def getP2(self):
        return self.p2

    def getSide(self):
        return self.side

    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def __str__(self):
        output = f"Square({self.p1}, {self.p2})"
        return output

    def setFillColour(self, colour):
        colours = ["red", "green", "blue", "yellow", "purple"]
        if colour in colours:
            self.fillColour = colour
    
    def setOutlineColour(self, colour):
        colours = ["red", "green", "blue", "yellow", "purple"]
        if colour in colours:
            self.outlineColour = colour

    def getPerimeter(self):
        return self.side * 4

    def getArea(self):
        return self.side * self.side

    def getCenter(self):
        if self.p1.getY() > self.p2.getY():
            ycenter = self.p1.getY() - self.side/2
        else:
            ycenter = self.p2.getY() - self.side/2

        if self.p1.getX() > self.p2.getX():
            xcenter = self.p1.getX() - self.side/2
        else:
            xcenter = self.p2.getX() - self.side/2
        
        return MyPoint(xcenter, ycenter)

    def scale(self, factor):
        self.side *= factor
        print("Side length:", self.side)
        self.p1 = MyPoint(self.p1.getX() - (self.side/4), self.p1.getY() - (self.side/4))
        print("P1:",self.p1)
        self.p2 = MyPoint(self.p1.getX() + self.side, self.p1.getY() + self.side)
        print("P2:", self.p2)
        newcenter = self.getCenter()
        print("New center:",newcenter)


class MyCircle:

    def __init__(self, center, radius):
        self.center = center
        self.radius = float(radius)

    def getCentre(self):
        return self.center
    
    def getRadius(self):
        return self.radius

    def move(self, dx, dy):
        self.center.move(dx,dy)

    def __str__(self):
        output = f"Circle({self.center},{self.radius})"
        return output


def testMyPoint():
    myPoint = MyPoint(100, 50)
    print("myPoint's x coordinate is", myPoint.getX())  # 100
    print("myPoint's y coordinate is", myPoint.getY())  # 50

    myPoint.move(10, -20)

    print("myPoint's x coordinate is", myPoint.getX())  # 110
    print("myPoint's y coordinate is", myPoint.getY())  # 30

    print("myPoint is:", myPoint)  # myPoint is: MyPoint(110, 30)


def testPoint():
    p = Point(100, 50)

    print("p is of type:", type(p))  # <class 'graphics.Point'>

    print("p's x coordinate is", p.getX())  # 100.0
    print("p's y coordinate is", p.getY())  # 50.0

    p.move(10, -20)

    print("p's x coordinate is", p.getX())  # 110.0
    print("p's y coordinate is", p.getY())  # 30.0

    print("p is:", p)  # p is: Point(110.0, 30.0)


def testSquare():
    p1 = MyPoint(100, 50)
    square = Square(p1, 50)
    print("square's side length is", square.getSide())  # 50
    print("square's p1 is", square.getP1())  # MyPoint(100, 50)
    print("square's p2 is", square.getP2())  # MyPoint(150, 100)

    square.move(10, -20)
    print("After the move ...")
    print("square's side length is", square.getSide())  # 50
    print("square's p1 is", square.getP1())  # MyPoint(110, 30)
    print("square's p2 is", square.getP2())  # MyPoint(160, 80)

    print(square)  # Square(MyPoint(110, 30), MyPoint(160, 80))

    print(f"Perimeter is {square.getPerimeter()}.")
    print(f"Area is {square.getArea()}.")

    center = square.getCenter()
    print(f"Center is {center}.")

    square.scale(2)

def testMyCircle():
    center = MyPoint(100,50)
    radius = 25
    circle = MyCircle(center, radius)
    print(circle)
    circle.move(10,-20)
    print(circle)


class BankAccount:

    def __init__(self, acc_holder, acc_name, ini_balance):
        self.acc_holder = acc_holder
        self.acc_name = acc_name
        self.balance = int(ini_balance)
        self.ini_balance = int(ini_balance)
        self.interest_rate = 0.04

    def getAccHolder(self):
        return f"Account holder name: {self.acc_holder}"

    def getAccName(self):
        return f"Account name: {self.acc_name}"
    
    def getIniBalance(self):
        return f"Initial balance: {self.ini_balance}"

    def getBalance(self):
        return f"Balance: {self.balance}"
    
    def setDeposit(self, deposit):
        self.balance += deposit
        return f"Balance after {deposit} deposit: {self.balance}"

    def setWithdrawal(self, withdrawal):
        if self.balance >= withdrawal:
            self.balance -= withdrawal
            return f"Balance after {withdrawal} withdrawal: {self.balance}"
        else:
            return f"Balance after attempted {withdrawal} withdrawal: {self.balance}"

    def __str__(self):
        output = f"Account name: {self.acc_name}, Account holder: {self.acc_holder} Balance: {self.balance}"
        return output

def testAccount():
    account = BankAccount("James McCann", "James McCann", 30)
    print(account.getAccHolder())
    print(account.getIniBalance())
    print(account.setDeposit(45))
    print(account.setWithdrawal(35))
    print(account.setWithdrawal(50))
    print(account.getAccName())
    print(account.getBalance())


class Aeroplane:

    def __init__(self, departure, destination):
        self.fuel = 0
        self.altitude = 0
        self.departure = departure
        self.destination = destination

    def setFuel(self, fuel):
        max_fuel = 150000
        if fuel <= max_fuel:
            self.fuel = fuel
            return self.fuel
        else:
            return "Too much fuel!"
    
    def increaseAlt(self, altitude):
        self.altitude += altitude
        return self.altitude

    def decreaseAlt(self, altitude):
        if self.altitude >= altitude:
            self.altitude -= altitude
            return self.altitude
        else:
            return "Too low!", self.altitude

    def setDeparture(self, departure):
        if self.departure != departure:
            self.departure = departure
            return self.departure
        else: 
            return "Already here"

    def setDestination(self, destination):
        if self.destination != destination:
            self.destination = destination
            return self.destination
        else:
            return "Already going here"
    
    def getDeparture(self):
        return self.departure
    
    def getDestination(self):
        return self.destination

    def getAltitude(self):
        return self.altitude

    def __str__(self):
        return f"Aeroplane:\nFuel: {self.fuel}, Altitude: {self.altitude}, Departure: {self.departure}, Destination: {self.destination}."


def testPlane():
    plane = Aeroplane("LAX", "EMA")
    plane.setFuel(150000)
    plane.increaseAlt(37500)
    print(plane)
    plane.decreaseAlt(37500)
    plane.setFuel(0)
    plane.setDeparture("EMA")
    plane.setDestination("N/A")
    print(plane)

testPlane()