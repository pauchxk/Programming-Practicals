from tkinter import *

class LoginApp:

    def __init__(self):
        self.win = Tk()
        self.win.title("Employee Login")
        self.win.geometry("250x100")
        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(column=0, row=0)
        self.mainFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.userName = StringVar()
        self.password = StringVar()
        self.message = StringVar()
        self.message.set("Enter username and password.")

    def createWidgets(self):
        lblMessage = Label(
            self.mainFrame,
            width=30,
            textvariable=self.message
        )
        lblMessage.grid(column=0, row=0, columnspan=2)

        lblUserName = Label(
            self.mainFrame,
            text="Username:"
        )
        lblUserName.grid(column=0,row=1)

        entryUserName = Entry(
            self.mainFrame,
            width=25,
            textvariable=self.userName
        )
        entryUserName.grid(column=1, row=1)

        lblPassword = Label(
            self.mainFrame,
            text="Password:"
        )
        lblPassword.grid(column=0, row=2)

        entryPassword = Entry(
            self.mainFrame,
            width=25,
            textvariable=self.password,
            show="*"
        )
        entryPassword.grid(column=1, row=2)

        btnSignIn = Button(
            self.mainFrame,
            text="Sign In",
            command=self.authenticate
        )
        btnSignIn.grid(column=0, row=3, padx=5, pady=5)

        btnCancel = Button(
            self.mainFrame,
            text="Cancel",
            command=self.win.destroy
        )
        btnCancel.grid(column=1, row=3, padx=5, pady=5)

    def authenticate(self):
        username = self.userName.get()
        password = self.password.get()

        loginDetails = {
            "YousefD": "VenterboSS",
            "SergeiT": "25Operyu",
            "Yemi": "Idec704",
            "WernerS": "IAmMel12"
        }
        
        if username not in loginDetails or loginDetails[username] != password:
            self.message.set("Incorrect username or password.")
            self.win.configure(background='red')
        else:
            self.message.set("Login successful!")
            self.win.configure(background='green')

    def run(self):
        self.createWidgets()
        self.win.mainloop()

def main():
    app = LoginApp()
    app.run()

main()