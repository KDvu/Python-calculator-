from tkinter import *
import sys

def num_press(num):
    print(num)

def clear():
    text.delete(0,END)
    return

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

text = Entry(frame,bd=20, insertwidth=1,font=30)
#text.config(state=DISABLED)
text.grid(row = 0, column = 0, columnspan = 5)

buttons = ["1","2","3","(",")",
           "4","5","6","x","/",
           "7","8","9","+","-",
           ".","0","CE","C","="]
i=0

button = []

for rows in range (1,5):
    for columns in range(5):
       button.append(Button(frame,text=buttons[i],padx=16,pady=16,bd=6,fg="black",command=lambda x=i: num_press(buttons[x])))
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