'''
H1e2l3l4o5w6o7r8l9d
'''

string = 'H1e2l3l4o5w6o7r8l9d5'
new_string = ''
for ip in range(len(string)):
  if ip%2==1:
    new_string += string[ip-1]*int(string[ip])
print(new_string)