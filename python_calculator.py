from tkinter import *
import sys

class Calculator():
    def __init__(self,display):
        self.total = 0
        self.current = 0
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False
        self.current_no = 1
        self.changeDisplay(0)

    def key_pressed(self, key):
        #if 0 <= int(key) <= 9:
        try:
            # check if the key pressed is a numer
            if isinstance(int(key), int):
                self.current_no+=1
                self.eq = False
                if display.get() == "0" or self.new_num == True:
                    display.delete(0,END)
                    display.insert(self.current_no,key)
                else:
                    self.new_num = False
                    display.insert(self.current_no,key)
                self.current = int(display.get())
                print(self.current)
        except ValueError:
            if key == "+" or key == "-" or key == "*" or key == "/":
                print("Operation: ", key)
                self.operation(key)
            elif key == ".":
                self.current_no+=1
                display.insert(self.current_no,key)
            elif key == "(" or key == ")":
                self.current_no+=1
                display.insert(self.current_no,key)
            elif key == "=":
                self.calculateTotal()
                print("equals")
            elif key == "C":
                self.clear()
            elif key == "CE":
                self.clear()

    def operation(self,op):
        if self.op_pending:
            self.calculate()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def calculate(self):
        if self.op == "+":
            self.total += self.current
        elif self.op == "-":
            self.total -= self.current
        elif self.op == "*":
            self.total *= self.current
        elif self.op == "/":
            self.total /= self.current
        self.new_num = True
        self.op_pending = False
        self.changeDisplay(self.total)

    def calculateTotal(self):
        self.eq = True
        if self.op_pending:
            self.calculate()
            self.changeDisplay(self.total)
        else:
            self.total = int(display.get())

    def changeDisplay(self,value):
        display.delete(0,END)
        display.insert(0, value)

    def clear(self):
        display.delete(0,END)
        display.insert(0, 0)

    def getNum(num):
        print("What is the %s number?" % (num))
        number = int(sys.stdin.readline())
        return number

    def add(n1,n2):
        print("%i + %i =" %(n1,n2), (n1+n2))
    def subtract(n1,n2):
        print("%i - %i =" %(n1,n2), (n1-n2))
    def multiply(n1,n2):
        print("%i * %i =" %(n1,n2), (n1*n2))
    def divide(n1,n2):
        print("%i / %i =" %(n1,n2), (n1/n2))

root = Tk()
root.title("Calculator")
frame =Frame(root)
frame.grid()

display = Entry(frame,bd=20, insertwidth=1,font=30)
#text.config(state=DISABLED)
display.grid(row = 0, column = 0, columnspan = 5)

calculator = Calculator(display)

buttons = ["1","2","3","(",")",
           "4","5","6","*","/",
           "7","8","9","+","-",
           ".","0","CE","C","="]
i=0

button = []

for rows in range (1,5):
    for columns in range(5):
       button.append(Button(frame,text=buttons[i],padx=16,pady=16,bd=6,fg="black",command=lambda x=i: calculator.key_pressed(buttons[x])))
       button[i].grid(row = rows, column = columns)
       i+=1


root.mainloop()

menu='''
(1)ADD
(2)SUBTRACT
(3)MULTIPLY
(4)DIVIDE
(5)EXIT
'''

'''
print(menu)


#input=int(sys.stdin.readline())
input=input("Choose an option:")

if input == "1":
    num1 = getNum("first")
    num2 = getNum("second")
    add(num1,num2)
elif input == "2":
    num1 = getNum("first")
    num2 = getNum("second")
    subtract(num1,num2)
elif input == "3":
    num1 = getNum("first")
    num2 = getNum("second")
    multiply(num1,num2)
elif input == "4":
    num1 = getNum("first")
    num2 = getNum("second")
    divide(num1,num2)
elif input == "5":
    print("Closing calculator")
    sys.exit
    '''