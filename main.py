from tkinter import Tk
from tkinter import Frame
from tkinter import Entry
from tkinter import Button
from calculator import Calculator

root = Tk()
root.title("Calculator")
frame = Frame(root)
frame.grid()

display = Entry(frame,bd=20, insertwidth=1,font=30)
display.config(state="disabled")
display.grid(row = 0, column = 0, columnspan = 5)

calculator = Calculator(display)

buttons = ["1","2","3","/-","<",
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