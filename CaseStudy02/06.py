'''
6.Please write a program thataccepts a string from the console and print it in reverse order.
Example: If the following string is given as input to the program: rise to vote sir
Then, the output of the program should be:ris etov ot esir
'''

string = 'rise to vote sir'

# Approach 01: By Slicing: 
print(string[::-1])

# Approach 02: Using For Loop with CDT:
reverse = ''
for ch in string:
  reverse = ch + reverse
print(reverse)

# Approach 03: Using For Loop with Range:
reverse = ''
for ip in range(-1, -(len(string))-1, -1):
  reverse += string[ip]
print(reverse)