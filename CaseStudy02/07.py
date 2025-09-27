'''
Please write a program that counts and prints the numbers of each character in a string input by the console.
Example: If the following string is given as input to the program:abcdefgabc
Then, the output of the program should be:
a2,2c,2b,2e,1d,1g,1f,1
'''

string = input('Enter A String: ')
charSet = set()
result = ''
for ch in string:
  if ch not in charSet:
    count = string.count(ch)
    result += f'{ch}{count}, '
    charSet.add(ch)
print(result)

  



