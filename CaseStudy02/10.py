'''
10.By using list comprehension, please write a program to print the list after removing the 0th,4th,and 5th numbers in [12,24,35,70,88,120,155].
'''

l = [12,24,35,70,88,120,155]
new_l = [l[ip] for ip in range(len(l)) if(ip not in (0,4,5))]
print(new_l)