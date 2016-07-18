import sys

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

menu='''
(1)ADD
(2)SUBTRACT
(3)MULTIPLY
(4)DIVIDE
(5)EXIT
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