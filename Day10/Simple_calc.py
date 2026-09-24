print("Welcome to the simple calculator!")
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
while True:
    a=int(input("Enter the first number: "))
    while True:
        op=input("Enter the operation (+, -, *, /): ")
        b=int(input("Enter the second number: "))
        if op=="+":
            print(f"{a} + {b} = {add(a,b)}")
        elif op=="-":
            print(f"{a} - {b} = {subtract(a,b)}")
        elif op=="*":
            print(f"{a} * {b} = {multiply(a,b)}")
        elif op=="/":
            print(f"{a} / {b} = {divide(a,b)}")
        c=input("Type 'y' you want to continue calculation on the same number, 'n' to start a new calculation or's' to exit:")
        if c=="y":
            continue
        elif c=="n":
            break
        elif c=="s":
            print("Thank you for using the simple calculator!")
            exit()            
        