from tkinter import *

class PosApp:

    def __init__(self):
        self.win = Tk()
        self.win.title("POS System")

        self.total = DoubleVar()
        self.total.set(0.00)
        
        self.newItemPrice = DoubleVar()

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        totalLabel = Label(
            self.win,
            text=f"Total Bill: ${self.total.get():.2f}"
        )
        totalLabel.pack()

        addItemButton = Button(
            self.win,
            command=lambda: self.createNewWin(totalLabel),
            text="Add Item"
        )
        addItemButton.pack()

    def createNewWin(self, totalLabel):
        newWin = Toplevel(self.win)
        newWin.title("Add Item to Bill")

        itemPriceLabel = Label(newWin, text="Item Price ($)")
        itemPriceLabel.pack()

        itemPriceEntry = Entry(
            newWin,
            textvariable=self.newItemPrice
        )
        itemPriceEntry.pack()

        addButton = Button(
            newWin,
            command=lambda: self.updateBill(totalLabel, newWin),
            text="Add to Bill"
        )
        addButton.pack()
        self.newItemPrice.set(0.00)

    def updateBill(self, totalLabel, newWin):
        newTotal = self.total.get() + self.newItemPrice.get()
        self.total.set(newTotal)
        totalLabel.config(text=f"Total Bill: ${self.total.get():.2f}")
        newWin.destroy()

    
def main():
    app = PosApp()
    app.run()

main()