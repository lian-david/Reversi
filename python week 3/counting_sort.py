#counting sort algorithm
#sorting array in descending order, array contains only numbers 4, 8, 12
#code is O(n) complexity, linear time

def count_sort(lst):
    count_4, count_8, count_12 = 0, 0, 0
    for i in lst:
        if i == 4:
            count_4 += 1
        elif i == 8:
            count_8 += 1
        elif i == 12:
            count_12 += 1
    result = [12 for count in range(count_12)] + [8 for count in range(count_8)] + [4 for count in range(count_4)]

    return result   #can also return immediately instead of storing in result

lst = [4, 8, 12, 8, 4, 8, 12]
print(count_sort(lst))
