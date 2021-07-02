import tkinter as tk
import random

#Constants declared here
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500

class Game(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        master.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        master.maxsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        master.title("Poker Game")
        self.pack()
        self.createWidgets()

### Functions for buttons check, bet, and fold ###
    def check_button(self):
        print("Button - Check")
    def bet_button(self):
        print("Button - Bet")
    def fold_button(self):
        print("Button - Fold")

    def createWidgets(self):
        topFrame = tk.Frame(self)
        buttonFrame = tk.Frame(self)
        bottomFrame = tk.Frame(self)

        topFrame.pack(side="top", fill="both", expand=True)
        buttonFrame.pack(side="top", fill="x", expand=True)
        bottomFrame.pack(side="bottom", fill="both", expand=True)

        listBox = tk.Listbox(topFrame, width=50)
        listBox.pack(side="top", fill="both", expand=True)

        tk.Button(buttonFrame, text="Check", command=self.check_button).grid(row=1, column=0)
        tk.Button(buttonFrame, text="Bet", command=self.bet_button).grid(row=1, column=1)
        tk.Button(buttonFrame, text="Fold", command=self.fold_button).grid(row=1, column=2)


app = Game(tk.Tk())
app.mainloop()