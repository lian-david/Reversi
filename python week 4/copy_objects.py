from copy import copy, deepcopy

lst = [[1, 2, 3], [4, 5, 6]]
lst2 = copy(lst)

# lst2[0][0] = 8
# print(lst)

lst3 = deepcopy(lst)
lst3[0][0] = 5
print(lst)
print(lst3)