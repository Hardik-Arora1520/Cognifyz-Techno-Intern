'''This program is of Create a Python program that converts
temperatures between Celsius and
Fahrenheit. Prompt the user to enter a
temperature value and the unit of
measurement, and then display the
converted temperature.
'''
print("The program of Temperature  Converter betweem C or F")
A=input("Enter the temperature:")
B=input("Enter the unit of  measurement (F or C):")
if  B=="F" or B=="f" :
    a=(float(A)-32)*5.0/9.0
    print("Temperature=", a," Celsius")
elif  B=="C" or B=="c":
    b=(float(A))*9.0/5.0+32
    print("Temperature=", b," Fahrenheit")