# Author: Ivana Irene Thomas / 1606887352 
#This program is a super calculator that have many amazing features in it
#Try and have fun
from tkinter import * #import all modules of tkinter
import math #import math moodules
from idlelib import ToolTip #import Tooltip module
class superCalculator: #define superclass
    def __init__(self): #construct the GUI
        window = Tk()
        window.title("Supercalculator [by Ivana Irene Thomas]")
        window.configure(bg="#f9f7e8")
        window.resizable(width=False, height=False) #make the window not resizeable
        entry = StringVar() #make entry box for user inputs
        self.entryBox = Entry(window,
                        relief=RIDGE, 
                        width = 35, 
                        borderwidth=3, 
                        font = ("System 20 bold"),
                        textvariable = entry)
        self.entryBox.grid(row=0, column=0, columnspan=5)
        buttons = [["CLR",  "MC",   "M+",   "M-",   "MR"], #make list of lists for button creation iteration
                    ["d",   "e",    "f",    "+",    "-" ],
                    ["a",   "b",    "c",    "/",    "*"],
                    ["7",   "8",    "9",    "**",   "\u221a"],
                    ["4",   "5",    "6",    "sin",  "cos"],
                    ["1",   "2",    "3",    "tan",  "ln"],
                    ["0",   ".",    "\u00b1",    "~",    "2C"],
                    ["x",   "o",    "^",    "|",    "&"],
                    ["π",   "int",  "rad",  "//",   "exp"],
                    ["bin", "hex",  "oct",  "%",    "="]]
        #make list of lists for tooltip
        tips = [["Clear the display field","Clear memory", "Add to memory", "Subtract from memory", "Recall from memory"],
                ["letter d", "letter e", "letter f", "add", "subtract"],
                ["letter a", "letter b", "letter c", "divide", "multiply"],
                ["digit 7", "digit 8", "digit 9", "power", "sqrt"],
                ["digit 4", "digit 5", "digit 6", "sine(radians)", "cosine(radians)"],
                ["digit 1", "digit 2", "digit 3", "tangent(radians)", "natural log"],
                ["digit 0", "decimal point", "toggle +- sign", "bitwise complement", "32 bit 2's Complement"],
                ["letter x", "letter o", "bitwise xor", "bitwise or", "bitwise and"],
                ["the number Pi", "truncate float to int", "convert degrees to radians", "integer divide", "exp"],
                ["bin", "hex", "oct", "modulus", "compute to decimal"]]
        self.memory = 0 #set the calculator's memory as 0
        self.expr = "" #set the expression empty
        self.startOfNextOperand = True 
        self.cleared = True         
        for r in range(10): #create the button using the list of lists defined
            for c in range(5):
                def cmd(x = buttons[r][c]):
                    self.click(x)
                b = Button(window, 
                            text=buttons[r][c], 
                            width = 7, 
                            relief = RAISED,
                            bg = "#62bfad",
                            fg = "#f9f7e8",
                            activebackground = "#f9f7e8",
                            activeforeground = "#62bfad",
                            font = ("System 14 bold"), 
                            command = cmd)
                b.grid(row=r+1, column = c)
                ToolTip.ToolTip(b, tips[r][c]) #add tooltip        
        window.mainloop()
        
    def click(self, key): #define a function that will convert whatever in the entry box into integer
        def kedecimal(x):
            if "0b" in x:
                return int(x,2)
            elif "0x" in x:
                return int(x,16)
            elif "0o" in x:
                return int(x,8)
            elif "." in x:
                return float(x)
            elif x == "e":
                return math.e
            else:
                return int(x)
        if key == "=": #define equal operation handler
            try:
                if len(self.expr) == 0:
                    result = self.entryBox.get()
                    self.entryBox.delete(0,END)
                    self.entryBox.insert(END, kedecimal(result))
                    self.startOfNextOperand = True
                else:
                    result = eval(self.expr+str(kedecimal(self.entryBox.get())))
                    self.entryBox.delete(0, END) 
                    self.entryBox.insert(END, result)
                    self.expr = ""
                    self.startOfNextOperand = True
            except:
                self.entryBox.delete(0, END)
                self.entryBox.insert(END, "Error")
                self.expr = ""
                self.startOfNextOperand = True
        #define handlers for operators
        elif key in "+*-/^|&%": 
            try:
                self.expr += str(kedecimal(self.entryBox.get()))
                self.expr += key
                self.startOfNextOperand = True
            except:
                self.expr += self.entryBox.get()
                self.expr += key
                self.startOfNextOperand = True

        elif key == "~": 
            try:
                self.expr += key
                self.expr += str(kedecimal(self.entryBox.get()))
                self.entryBox.delete(0, END)
                self.entryBox.insert(END, eval(self.expr))
                self.expr = ""
                self.startOfNextOperand = True
            except:
                self.entryBox.insert(END, "Error")
                self.startOfNextOperand = True
        elif key == "//":
            try:
                self.expr += str(kedecimal(self.entryBox.get()))
                self.expr += key
                self.startOfNextOperand = True
            except:
                self.expr += self.entryBox.get()
                self.expr += key
                self.startOfNextOperand = True
        elif key == "\u221a":
            try:
                result = math.sqrt(kedecimal(self.entryBox.get()))
                self.entryBox.delete(0, END)
                self.entryBox.insert(END, result)
                self.startOfNextOperand = True  
            except:
                self.entryBox.delete(0,END)
                self.entryBox.insert(END, "Error")
                self.startOfNextOperand = True
        elif key == "\u00b1":
            try:
                if self.entryBox.get()[0] == "-":
                    self.entryBox.delete(0)
                else:
                    self.entryBox.insert(0, "-")
            except:
                self.entryBox.insert(END, "Error")
        
        elif key == "π":
            self.entryBox.delete(0,END)
            self.entryBox.insert(END,math.pi)
            self.startOfNextOperand = True
        elif key == "**":
            try:
                self.expr += str(kedecimal(self.entryBox.get()))
                self.expr += key
                self.startOfNextOperand = True
            except:
                self.startOfNextOperand = True
        elif key == "sin":
            try:
                result = math.sin(kedecimal(self.entryBox.get()))
                self.entryBox.delete(0, END)
                self.entryBox.insert(END, result)
                self.startOfNextOperand = True  
            except:
                self.entryBox.delete(0,END)
                self.entryBox.insert(END, "Error")
                self.startOfNextOperand = True
        
        elif key == "cos":
            try:
                result = math.cos(kedecimal(self.entryBox.get()))
                self.entryBox.delete(0, END)
                self.entryBox.insert(END, result)
                self.startOfNextOperand = True  
            except:
                self.entryBox.delete(0,END)
                self.entryBox.insert(END, "Error")
                self.startOfNextOperand = True
        elif key == "tan":
            try:
                result = math.tan(kedecimal(self.entryBox.get()))
                self.entryBox.delete(0, END)
                self.entryBox.insert(END, result)
                self.startOfNextOperand = True  
            except:
                self.entryBox.delete(0,END)
                self.entryBox.insert(END, "Error")
                self.startOfNextOperand = True
        
        elif key == "ln":
            try:
                result = math.log(kedecimal(self.entryBox.get()))
                self.entryBox.delete(0, END)
                self.entryBox.insert(END, result)
                self.startOfNextOperand = True  
            except:
                self.entryBox.delete(0,END)
                self.entryBox.insert(END, "Error")
                self.startOfNextOperand = True

        elif key == "bin":
            try:
                result = bin(kedecimal(self.entryBox.get()))
                self.entryBox.delete(0, END)
                self.entryBox.insert(END, result)
                self.startOfNextOperand = True  
            except:
                self.entryBox.delete(0,END)
                self.entryBox.insert(END, "Error")
                self.startOfNextOperand = True
        elif key == "oct":
            try:
                result = oct(kedecimal(self.entryBox.get()))
                self.entryBox.delete(0, END)
                self.entryBox.insert(END, result)
                self.startOfNextOperand = True  
            except:
                self.entryBox.delete(0,END)
                self.entryBox.insert(END, "Error")
                self.startOfNextOperand = True
        elif key == "int":
            try:
                result = kedecimal(self.entryBox.get())
                self.entryBox.delete(0, END)
                self.entryBox.insert(END, result)
                self.startOfNextOperand = True  
            except:
                self.entryBox.delete(0,END)
                self.entryBox.insert(END, "Error")
                self.startOfNextOperand = True
        elif key == "hex":
            try:
                result = hex(kedecimal(self.entryBox.get()))
                self.entryBox.delete(0, END)
                self.entryBox.insert(END, result)
                self.startOfNextOperand = True  
            except:
                self.entryBox.delete(0,END)
                self.entryBox.insert(END, "Error")
                self.startOfNextOperand = True
        elif key == "rad":
            try:
                result = math.radians(kedecimal(self.entryBox.get()))
                self.entryBox.delete(0, END)
                self.entryBox.insert(END, result)
                self.startOfNextOperand = True  
            except:
                self.entryBox.delete(0,END)
                self.entryBox.insert(END, "Error")
                self.startOfNextOperand = True
        elif key == "exp":
            try:
                result = math.exp(kedecimal(self.entryBox.get()))
                self.entryBox.delete(0, END)
                self.entryBox.insert(END, result)
                self.startOfNextOperand = True  
            except:
                self.entryBox.delete(0,END)
                self.entryBox.insert(END, "Error")
                self.startOfNextOperand = True
        elif key == "2C":
            complement = {"1":"0", "0":"1"} #make dictionary to swap characters for further use
            try:
                if kedecimal(self.entryBox.get()) > 0: #case if it's a positive number
                    result = kedecimal(self.entryBox.get()) #get the characters in entry box and convert it to integers
                    result = bin(result) #convert to binary
                    result = result[2:] #take the binary number without the "0b"
                    result = list(result) #seperate the binary number into list
                    result = "".join(complement[x] for x in result) #convert the characters taking from the complement dictionary and join them back to string
                    hasil = bin(int(result,2) + int("01",2)) #add 1
                    if len(hasil[2:]) < len(result): #make the exception for when the bits of binary decreases when added by one
                        hasil = hasil[2:].rjust(len(result),"0")
                    else:
                        hasil = hasil[2:] #take the binary number without the "0b"
                    hasil = "0b"+hasil.rjust(32,"1") #display the result in 32 bits
                    self.entryBox.delete(0,END)
                    self.entryBox.insert(END, hasil)
                else:
                    biner = bin(abs(kedecimal(self.entryBox.get()))) #case if it's negative number
                    hasil = biner[0:2]+biner[2:].rjust(32,"0") 
                    self.entryBox.delete(0,END)
                    self.entryBox.insert(END, hasil)
                self.startOfNextOperand = True
            except:
                self.entryBox.delete(0,END)
                self.entryBox.insert(END, "Error")
                self.startOfNextOperand = True
        elif key == "CLR": 
            self.entryBox.delete(0, END)
            self.expr = ""
        elif key =="MC":
            self.memory = 0
            self.cleared = True
        elif key == "M+":
            try:
                self.memory += kedecimal(self.entryBox.get())
                self.cleared = False
            except:
                self.entryBox.delete(0,END)
                self.entryBox.insert(END, "Error")
                self.startOfNextOperand = True       
        elif key == "M-": 
            try:
                self.memory -= kedecimal(self.entryBox.get())
                self.cleared = False
            except:
                self.entryBox.delete(0,END)
                self.entryBox.insert(END, "Error")
                self.startOfNextOperand = True
        elif key == "MR":
            if self.cleared:
                self.entryBox.delete(0,END)
                self.entryBox.insert(END,"")
            else:
                self.entryBox.delete(0,END)
                self.entryBox.insert(END,self.memory)
        else:
            if self.startOfNextOperand:
                self.entryBox.delete(0, END)
                self.startOfNextOperand = False
            self.entryBox.insert(END,key)
superCalculator()



