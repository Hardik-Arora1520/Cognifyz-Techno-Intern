print('Task of fibonacci sequence')
def fibo(n):
    a=0
    b=1
    if n==1:
        print('Fibonaci sequence till',n,'is: ',a)
    elif n==2:
        print('Fibonaci sequence till',n,'is: ',a)
        print(b)
    else:
        print('Fibonaci sequence till',n,'is: ',a)
        print(b)
        for i in range(n-2):
            c=a+b
            print(c)
            a=b
            b=c
n=int(input("Enter the number of terms you want to display in Fibonacci series :"))
fibo(n)