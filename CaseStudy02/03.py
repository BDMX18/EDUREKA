'''
A website requires a user to input a username and password to register. Write a program to check the validity of the password given by the user. Following are the criteria for checking password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]1. At least 1 letter between [A-Z]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12
'''

def valid_password(password):

  if len(password) < 6 or len(password) > 12:
    return False

  has_lower = False
  has_upper = False
  has_digit = False
  has_special = False

  special_char = '$#@'

  for char in password:
    if 'a' <= char <= 'z':
      has_lower = True
    elif 'A' <= char <= 'Z':
      has_upper = True
    elif '0' <= char <= '9':
      has_digit = True
    elif char in special_char:
      has_special = True

  return has_lower and has_upper and has_digit and has_special

username = input('Enter Your Username: ')
password = input('Enter A Password: ')

if(valid_password(password)):
  print(f'{username}, Your Password is Valid!')
else:
  print(f'{username}, Your Password is Invalid!')
