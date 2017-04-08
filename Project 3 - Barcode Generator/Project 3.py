from tkinter import * #import all tkinter modules

invalid_chars = "/?<>\:*|\"" #define invalid chars for further use in file name's character exception

#make a dictionary for the pattern of barcode, and the decoding of every digit
LcodeDict = {"0":"0001101", "1":"0011001", "2":"0010011", "3":"0111101", "4":"0100011", "5":"0110001", "6":"0101111", "7":"0111011", "8":"0110111", "9":"0001011"}
RcodeDict = {"0":"1110010", "1":"1100110", "2":"1101100", "3":"1000010", "4":"1011100", "5":"1001110", "6":"1010000", "7":"1000100", "8":"1001000", "9":"1110100"}
GcodeDict = {"0":"0100111", "1":"0110011", "2":"0011011", "3":"0100001", "4":"0011101", "5":"0111001", "6":"0000101", "7":"0010001", "8":"0001001", "9":"0010111"}
FirstsixDict = {"0":"LLLLLL", "1":"LLGLGG", "2":"LLGGLG", "3":"LLGGGL", "4":"LGLLGG", "5":"LGGLLG", "6":"LGGGLL", "7":"LGLGLG", "8":"LGLGGL", "9":"LGGLGL"}
def checkDigit(x): #define the function to count the check digit
        digit = [int(i) for i in x]
        a = (digit[0]+digit[2]+digit[4]+digit[6]+digit[8]+digit[10])
        b = (digit[1]+digit[3]+digit[5]+digit[7]+digit[9]+digit[11])
        c = (a+b*3)
        if c%10 == 0:
            result = "0"
        else:
            result = str(10-(c%10))
        return result
#create a new class to process barcode
class processBarcode:    
    def process(inp):
            string=inp+str(checkDigit(inp)) 
            formatDepan = (FirstsixDict[(string[0])])
            stringbaru = string[1:] #make the barcode starting from the first digit to the last digit plus the check digit
            x,y = 0,0
            barcode = "" #iterate through the barcode and decode it to EAN-13 format
            for i in formatDepan:
                if i == "L":
                    digit = LcodeDict[stringbaru[x]]
                elif i == "G":
                    digit = GcodeDict[stringbaru[x]]
                x+=1
                barcode = barcode+digit

            y = 6
            for i in range(len(stringbaru[6:])):
                digit = RcodeDict[stringbaru[y]]
                barcode = barcode+digit
                y+=1
            return barcode
    def check(inp):
        return inp+str(checkDigit(inp))  #a function to return barcode plus the checkdigit
    
#define a class     
class BarcodeWriter(processBarcode):
    def __init__(self):
        master = Tk() #assign the Tk() module to a variable called master
        master.title("EAN-13 by Ivana Irene Thomas") #create title for tkinter window
        master.resizable(width=False, height=False) #make the window not resizeable
        text1 = Label(text="Save barcode to PS file [eg: EAN13.eps]:",font=("Helvetica 12 bold")) #make label and change its properties 
        text1.pack() #pack the label into the master 
        self.entry = StringVar() #assign a string variable to the self.entry variable
        self.enterFilename = Entry(master, textvariable=self.entry) #create an entry box, put it on master and declare its text variable properties self.entry
        self.enterFilename.bind("<Return>", self.enter) #bind the entry box and enter key to function enter
        self.enterFilename.pack() #pack the entry box
        text2 = Label(text="Enter code (first decimal digits):",font=("Helvetica 12 bold")) #create another label
        text2.pack() #pack the label to the master
        self.barcode = StringVar() #assign a string variable to the self.barcode variable
        self.enterBarcode = Entry(master, textvariable=self.barcode) #create another entry box, put it on master and declre its text variable properties self.barcode
        self.enterBarcode.bind("<Return>", self.enter) #bind the entry box and enter key to function enter
        self.enterBarcode.pack() #pack the entry box to the master
        self.canvas = Canvas(master, width=250, height=350, bg="white") #create a canvas and declare its height and width
        self.canvas.pack() #pack the canvas to the master
        master.mainloop()

    def enter(self, event):
        self.name = self.entry.get() #get the string input of the entry box self.entry and assign it to self.name
        inp = self.barcode.get() #get the string input of the entry box self.barcode and assign it to inp
        for i in invalid_chars: #iterate through invalid chars and find whether self.name have it
            if i in self.name:
                messagebox.showwarning( #show warning message box when user inputs invalid file name
                "Invalid File Name",
                "Please enter a valid file name")
                return
                                    
                
        if self.name[-4:] != ".eps": #show warning when user doesn't input the file name with .eps as its extension
            messagebox.showwarning(
            "Invalid File Name",
            "Please enter a valid file name"
        )
        elif len(inp)!=12 or not inp.isdigit(): #show warning when user doesn't input a valid barcode 
            messagebox.showwarning(
            "Invalid Barcode",
            "Please enter a valid barcode number")
        else:
            self.canvas.delete("all") #delete canvas at every enter pressed and continue
            barcode=processBarcode.process(inp)
            string=processBarcode.check(inp) 
            #create text inside the canvas
            title = self.canvas.create_text(29,50, anchor="nw",text="EAN-13 Barcode:", font=("Helvetica 19 bold"))

            #make the starting lines of barcode
            self.canvas.create_line(30, 100, 30, 240, fill = "brown", tags = "Line", width=2)
            self.canvas.create_line(32, 100, 32, 240, fill = "white", tags = "Line", width=2)
            self.canvas.create_line(34, 100, 34, 240, fill = "brown", tags = "Line", width=2)
            x = 36
            #iterate through the second to the sixth digit of barcode and make the lines of barcode according to the decoded EAN-13
            #make black lines for every 1s, and white for every 0s
            for k in barcode[0:42]:
                if k =="1":
                    self.canvas.create_line(x, 100, x, 230, fill = "brown", tags = "Line", width=2)
                elif k == "0":
                    self.canvas.create_line(x, 100, x, 230, fill = "white", tags = "Line", width=2)
            
                x+=2
            #make the middle pattern lines of barcode
            x+=2
            self.canvas.create_line(x, 100, x, 240, fill = "white", tags = "Line", width=2)
            x+=2
            self.canvas.create_line(x, 100, x, 240, fill = "brown", tags = "Line", width=2)
            x+=2
            self.canvas.create_line(x, 100, x, 240, fill = "white", tags = "Line", width=2)
            x+=2
            self.canvas.create_line(x, 100, x, 240, fill = "brown", tags = "Line", width=2)
            x+=2
            self.canvas.create_line(x, 100, x, 240, fill = "white", tags = "Line", width=2)
            x+=2

            #iterate through the last six digits of barcode and make the lines of barcode according to the decoded EAN-13
            #make black lines for every 1s, and white for every 0s
            for k in barcode[42:]:
                if k =="1":
                    self.canvas.create_line(x, 100, x, 230, fill = "brown", tags = "Line", width=2)
                elif k =="0":
                    self.canvas.create_line(x, 100, x, 230, fill = "white", tags = "Line", width=2)
                x+=2
            #make the end pattern lines of barcode
            x+=2
            self.canvas.create_line(x, 100, x, 240, fill = "brown", tags = "Line", width=2)
            x+=2
            self.canvas.create_line(x, 100, x, 240, fill = "white", tags = "Line", width=2)
            x+=2
            self.canvas.create_line(x, 100, x, 240, fill = "brown", tags = "Line", width=2)
            #create text for informing user of the check digit
            tulisan = self.canvas.create_text(24, 245, anchor="nw",text="{} {} {}".format(string[0], string[1:7], string[7:]), font=("Helvetica 19 bold"), justify="center")
            check = self.canvas.create_text(55, 295, anchor="nw",text="Check Digit: {}".format(checkDigit(inp)), font=("Helvetica 14 bold"), fill="orange")   
            self.canvas.postscript(file=self.name, colormode='color')
BarcodeWriter()
