'''Made a Python function that evaluates
the strength of a password entered by the
user. Implement checks for factors such as
length, presence of uppercase and
lowercase letters, digits, and special
characters.'''
def pass_checker(password):
    uppercase = 0
    lowercase = 0
    digit = 0
    special_char = 0
    length = len(password)
    
    if length < 8:
        print('Password must be at least 8 characters long')
    else:
        for char in password:
            if char.islower():
                lowercase += 1
            elif char.isupper():
                uppercase += 1
            elif char.isdigit():
                digit += 1
            elif char in '!@#$%^&*()':
                special_char += 1
    if uppercase > 0 and lowercase > 0 and digit > 0 and special_char > 0:
        print('Password strength is strong')
    elif uppercase > 0 and lowercase > 0 or digit > 0 or special_char > 0:
        print('Password strength is Fair')
    else:
        print('Password strength is weak')

password = input("Enter your password: ")
pass_checker(password)
