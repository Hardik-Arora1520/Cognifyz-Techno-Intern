'''this file contain Task of Develop a Python function that validates
whether a given string is a valid email
address. Implement checks for the format,
including the presence of an "@" symbol and
a domain name'''
print("Program for Email  Validator")
def Valid(email):
    if '@' not in email and  '.' not in email and  len(email) < 6 and 'com' not in email or 'org' not in email or "in" not in email:
        return False
    temp = email.split('@')[1]
    if len(temp.split('.')) <2:
        return False
    return True
email = input("Enter the email : ")
if Valid(email):
    print("The entered email id is valid")
else:
    print("Please enter the valid email id")