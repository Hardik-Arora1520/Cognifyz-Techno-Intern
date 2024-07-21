'''This is the Program containing Create a Python program that acts as a basic
calculator. It should prompt the user to
enter two numbers and an operator, and then display the result of the
operation.'''
print("Creating a calculator program")
def calculator(a,b):
    if n=="+":
        print("a+b=",a+b)
    elif n=="-":
        print ("a-b= ",a-b)
    elif n=="*":
        print ("a*b=" ,a*b)
    elif n=="/":
        print ("a/b=",a/b)
    elif  n=="%":
        print("a%b=",a%b)
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
n=input("Enter the operator(+,-,*,/,%):")
calculator(a,b)