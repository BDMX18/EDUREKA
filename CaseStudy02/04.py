'''
4.Write a for loop that prints all elements of a list and their position in the list.
a = [4,7,3,2,5,9] 
Hint: Use Loop to iterate through list elements.
'''

a = [4,7,3,2,5,9] 
for ip in range(len(a)):
  print(f'Index Position {ip}, Element is {a[ip]}')

# Using while loop:
print()
ip = 0
while ip < len(a):
  print(f'Index Position {ip}, Element Is {a[ip]}')
  ip += 1
