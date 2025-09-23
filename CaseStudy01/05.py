'''
5. Design a code that will find whether the given number is a Palindrome number or
not.
Hint: Use built-in functions of string.
'''

num = int(input('Enter A Number: '))
# reverse = 0
# dummy = num
# while dummy > 0:
#   rem = dummy % 10
#   reverse = reverse * 10 + rem
#   dummy //= 10
# if(num == reverse):
#   print('Palindrome Number')
# else:
#   print('Not A Palindrome Number')

num_str = str(num)
if(num == int(num_str[::-1])):
  print('Palindrome')
else:
  print('Not Palindrome')