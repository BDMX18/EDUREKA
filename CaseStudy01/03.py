'''
3. Write a program, which will find all the numbers between 1000 and 3000 (both
included) such that each digit of a number is an even number. The numbers
obtained should be printed in a comma-separated sequence on a single line.
Hint: In case of input data being supplied to the question, it should be assumed to
be a console input. Divide each digit with 2 and verify is it even or not.
'''

num_string = ''
for num in range(1000, 3001):
  dummy = num
  while dummy > 0:
    rem = dummy % 10
    dummy //= 10
    if(rem%2!=0):
      break
  else:
    num_string += str(num) + ', '
print(num_string)
