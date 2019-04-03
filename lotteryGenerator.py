"""
Program: lotteryGenerator.py 
Author: James Jutt
Date: 3/27/19

Lottery Number Generator
Create a GUI-based python program that will display a label at the top that says something to the effect of "Lottery Numbers", or "Lottery Number Generator", 
have 5 number fields in the GUI that will accept the output. 
And have a command button that when clicked, will generate the 5 random numbers between 1 and 55 and place the numbers in the fields for output. 
Use color and GUI design elements to make the program look appealing and easy to use. 
Yes, this is a previous classes final that I had showed you examples of yesterday and a few times before. 
You can use the book, past projects, any resource you would like to help you with this project.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from PIL import ImageTk,Image
from tkinter.font import Font
import random

class LotteryGenerator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Lottery Number Generator", width = 650, height = 500, resizable = False, background = "black")
        myFont = Font(family = "Arial Black", size = 25, slant = "italic")
        # Image Panel
        imageLabel = self.addLabel(text = "", row = 1, column = 0, columnspan = 5, background = "black")
        self.image = ImageTk.PhotoImage(Image.open("lottery.jpg"))
        imageLabel["image"] = self.image

        outputPanel = self.addPanel(row = 2, rowspan = 2, column = 0, columnspan = 5, background = "black")
        self.numOne = self.addLabel(text = "00", row = 2, column = 0, foreground = "red", background = "black", font = myFont, sticky = "NSEW")
        self.numTwo = self.addLabel(text = "00", row = 2, column = 1, foreground = "yellow", background = "black", font = myFont, sticky = "NSEW")
        self.numThree = self.addLabel(text = "00", row = 2, column = 2, foreground = "green", background = "black", font = myFont, sticky = "NSEW")
        self.numFour = self.addLabel(text = "00", row = 2, column = 3, foreground = "blue", background = "black", font = myFont, sticky = "NSEW")
        self.numFive = self.addLabel(text = "00", row = 2, column = 4, foreground = "purple", background = "black", font = myFont, sticky = "NSEW")
        
        self.randomBtn = self.addButton(text = "Click here to generate your 5 winning lottery numbers!", row = 3, rowspan = 5, column = 0, columnspan = 6, command = self.randomize)
        self.randomBtn["font"] = Font(family = "Arial Black", size = 21, slant = "italic")
        self.randomBtn["background"] = "black"

    def randomize(self):
        self.numOne["text"] = random.randint(1, 55)
        self.numTwo["text"] = random.randint(1, 55)
        self.numThree["text"] = random.randint(1, 55)
        self.numFour["text"] = random.randint(1, 55)
        self.numFive["text"] = random.randint(1, 55)

def main():
    LotteryGenerator().mainloop()

main()