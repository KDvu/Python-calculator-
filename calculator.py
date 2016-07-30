from tkinter import END

class Calculator():
    def __init__(self,display):
        self.total = 0
        self.current = 0
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False
        self.current_no = 1
        self.display = display
        self.changeDisplay(0)

    def key_pressed(self, key):
        try:
            # check if the key pressed is a numer
            if isinstance(int(key), int):
                self.current_no+=1
                self.eq = False
                if self.display.get() == "0" or self.new_num == True:
                    self.display.config(state="normal")
                    self.display.delete(0,END)
                    self.display.insert(self.current_no,key)
                    self.display.config(state="disabled")
                    self.new_num = False
                else:
                    self.display.config(state="normal")
                    self.display.insert(self.current_no,key)
                    self.display.config(state="disabled")
                    self.new_num = False

                self.current = float(self.display.get())
        except ValueError:
            if key == "+" or key == "-" or key == "*" or key == "/":
                self.operation(key)
            elif key == ".":
                self.current_no+=1
                self.new_num = False
                self.display.config(state="normal")
                self.display.insert(self.current_no, key)
                self.display.config(state="disabled")
            elif key == "/-":
                self.sign()
            elif key == "<":
                self.new_num = False
                self.deleteNum()
            elif key == "=":
                self.calculateTotal()
            elif key == "C":
                self.clear()
            elif key == "CE":
                self.clearAll()

    def operation(self,op):
        if self.op_pending:
            self.calculate()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def sign(self):
        self.current = -float(self.display.get())
        self.changeDisplay(int(self.current))

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
            self.total = float(self.display.get())

    def changeDisplay(self,value):
        self.display.config(state="normal")
        self.display.delete(0,END)
        self.display.insert(0, value)
        self.display.config(state="disabled")

    def deleteNum(self):
        s = self.display.get()
        s = s[:-1]
        if not s:
            self.changeDisplay(0)
        else:
            self.changeDisplay(s)
        self.current = float(self.display.get())

    def clear(self):
        self.current = 0
        self.current_no = 1
        self.new_num = True
        self.display.config(state="normal")
        self.display.delete(0,END)
        self.display.insert(0, 0)
        self.display.config(state="disabled")

    def clearAll(self):
        self.clear()
        self.eq = False
        self.total = 0
        self.op_pending = False