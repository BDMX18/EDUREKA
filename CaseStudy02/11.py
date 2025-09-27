'''
11.By using list comprehension, please write a program to print the list after removing deleted numbers that are divisible by 5 and 7 in [12,24,35,70,88,120,155].
'''

L = [12,24,35,70,88,120,155]
new_L = [item for item in L if item%5 != 0 and item%7 != 0]
print(new_L)