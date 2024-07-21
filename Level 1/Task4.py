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