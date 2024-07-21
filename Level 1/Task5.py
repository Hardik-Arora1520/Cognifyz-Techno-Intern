'''The task of Write a Python function that checks whether
a given string is a palindrome. A palindrome
is a word, phrase, or sequence that reads the
same backward as forward'''
print("Palindrome Checker")
def Backward(input_string):
    return input_string[::-1]
I=input("Enter a Word/Name: ")
Backward(I)
if I==Backward(I):
    print('The word',I, 'is Palindrome having backword  as ',Backward(I))
else:
    print('The word',I,' is not Palindrome because its reverse',Backward(I),'is note same')
