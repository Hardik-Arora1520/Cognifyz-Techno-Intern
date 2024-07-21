'''This is the task of Creating a Python function that takes a
string as input and returns the reverse of
that string.
 '''
print("String reversal Task")
def reversal(input_string):
    return input_string[::-1]
p=reversal(input("Enter the Data:-"))
print("Reverse of data:-",p)