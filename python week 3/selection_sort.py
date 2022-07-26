def selection_sort(lst):
    for i in range(len(lst) - 1):
        min_index = i

        #find the minimum value in lst[i + 1 ... n - 1]
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        #swap the minimum value with element number i
        lst[i], lst[min_index] = lst[min_index], lst[i]

lst = [4, 8, 2, 10, 5, 6, 3]
selection_sort(lst)
print(lst)
