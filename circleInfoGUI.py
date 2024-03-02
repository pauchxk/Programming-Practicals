from tkinter import *
from math import pi

class CircleCalculator:

    def __init__(self):
        self.win = Tk()
        self.win.title("Circle Info")
        self.win.geometry("250x250")
        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(column=0, row=0)
        self.mainFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.radius = StringVar()
        self.message = StringVar()
        self.message.set("Radius in cm:")
        self.area = StringVar()
        self.area.set("Area: ")
        self.circumference = StringVar()
        self.circumference.set("Circumference: ")

    def createWidgets(self):
        lblMessage = Label(
            self.mainFrame,
            width=15,
            textvariable=self.message
        )
        lblMessage.grid(column=0, row=0, columnspan=2)

        entryRadius = Entry(
            self.mainFrame,
            width=10,
            textvariable=self.radius
        )
        entryRadius.grid(column=0, row=1)

        lblArea = Label(
            self.mainFrame,
            width=15,
            textvariable=self.area
        )
        lblArea.grid(column=0, row=2)

        lblCircumference = Label(
            self.mainFrame,
            width=20,
            textvariable=self.circumference
        )
        lblCircumference.grid(column=0, row=3)

        btnCalculate = Button(
            self.mainFrame,
            text="Calculate",
            command=self.calculate
        )
        btnCalculate.grid(column=0, row=4,)

        btnClose = Button(
            self.mainFrame,
            text="Close",
            command=self.win.destroy
        )
        btnClose.grid(column=0, row=5)

    def calculate(self):
        radius = float(self.radius.get())
        circumference = 2 * pi * radius
        self.circumference.set(f"Cirumference: {circumference:.2f}cm")
        area = pi * radius**2
        self.area.set(f"Area: {area:.2f}cm^2")

    def run(self):
        self.createWidgets()
        self.win.mainloop()

def main():
    app = CircleCalculator()
    app.run()

main()