'''
1. Write a program that will find factors of the given number and find whether
the factor is even or odd.
Hint: Use Loop with if-else statements
'''

num = int(input('Enter A Number: '))
factorial = 1
for i in range(num, 1, -1):
  factorial *= i
print(F'Factorial of {num} is {factorial}')
if factorial % 2 == 0:
  print('Factorial Is A Even Number!')
else:
  print('Factorial Is A Odd Number!')