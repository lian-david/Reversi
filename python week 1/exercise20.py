#write program to convert a given list of tuples into a list of lists

t_lst = [(1,2), (2,3), (3,4)] 
lst = [list(item) for item in t_lst]
print(lst)