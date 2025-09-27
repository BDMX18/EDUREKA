'''
5.Please  write  a  program that accepts a string from the console and print the characters that have even indexes.
Example: If the following string is given as input to the program:H1e2l3l4o5w6o7r8l9d
Then, 
the output of the program should be:Helloworld
'''

string = input('Enter A Stirng: ')
for_string = ''
for ip in range(len(string)):
  if(ip%2 == 0):
    for_string += string[ip]
print('New String:', for_string)

while_string = ''
ip = 0
while ip < len(string):
  if (ip % 2 == 0):
    while_string += string[ip]
  ip += 1
print('New String:', while_string)
