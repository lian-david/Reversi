def sequence(lst):
    lst = sorted(lst)

    left = 0
    right = len(lst) - 1
    seq = (lst[-1] - lst[0]) // len(lst)

    while left < right:
        mid = (left + right) // 2
        if mid + 1 < len(lst) and lst[mid + 1] - lst[mid] != seq:
            return lst[mid + 1] - seq

        if mid - 1 > 0 and lst[mid] - lst[mid - 1] != seq:
            return lst[mid - 1] + seq

        if lst[mid] - lst[0] != (mid - 0) * seq:
            right = mid + 1

    return -1
    
lst1 = [12, 3, 6, 15, 18]
print(sequence(lst1))

def shell_sort(lst):
    gap = (len(lst)) // 2
    while gap > 0:
        for i in range(gap, len(lst)):
            key = lst[i]
            j = i
            while (j >= gap) and (lst[j - gap] > key):
                 lst[j] = lst[j - gap]
                 j = j - gap
            lst[j] = key
        gap = gap // 2

A = [9, 8, 3, 7, 5, 6, 4, 1]
shell_sort(A)
print(A)

