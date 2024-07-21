print("Palindrome Checker")
def Backward(input_string):
    return input_string[::-1]
I=input("Enter a Word/Name: ")
Backward(I)
if I==Backward(I):
    print('The word',I, 'is Palindrome having backword  as ',Backward(I))
else:
    print('The word',I,' is not Palindrome because its reverse',Backward(I),'is note same')
