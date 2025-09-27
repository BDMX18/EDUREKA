'''
8.
With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],   
write   a program to make a list whose elements are intersection of the above given lists.
'''

list_one = [1,3,6,78,35,55]
list_two = [12,24,35,24,88,120,155]
intersection_list = []
for lo_e in list_one:
  for lt_e in list_two:
    if lo_e == lt_e and lo_e not in intersection_list:
      intersection_list.append(lo_e)
print(intersection_list)

intersection_list = list(set(list_one) & set(list_two))
print(intersection_list)