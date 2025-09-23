'''
Write a program that accepts a sentence and calculates the number of letters
and digits.
Suppose if the entered string is: Python0325
Then the output will be:
LETTERS: 6
DIGITS:4
Hint: Use built-in functions of string.
'''

string = input('Enter A String: ')
letter_count = 0
digit_count = 0
for char in string:
  if(char.isalpha()):
    letter_count += 1
  else:
    digit_count += 1
print('LETTERS: ',letter_count)
print('DIGITS: ',digit_count)