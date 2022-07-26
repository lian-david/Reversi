#A magic index in an array A is defined to be an index i such that A[i] = i
# Given a sorted array A of distinct integers, write an efficient method to find 
# a magic index in A, if one exists

#simplest solution
def magic_index(a):
    for i in range(len(a)):
        if a[i] == i:
            return a[i]
    return -1

lst1 = [-1, 0, 1, 2, 4, 10]
lst2 = [-10, -1, 0, 3, 10, 11, 30]

print(magic_index(lst1))
print(magic_index(lst2))

#binary search solution
def magic_idx(a, left, right):
    if left >= right:
        return -1

    mid = (left + right) // 2
    if a[mid] == mid:
        return mid
    elif a[mid] >= mid:
        return magic_idx(a, left, mid - 1)
    elif a[mid] <= mid:
        return magic_idx(a, mid + 1, right)



print(magic_idx(lst1, 0, len(lst1) - 1))
print(magic_idx(lst2, 0, len(lst2) - 1))

#correction:
def mag_index_rec(A, left, right):
    #base case: if left > right we have an empty list 
    if left > right:
        return None

    mid = (left + right) // 2
    if A[mid] == mid:
        return mid
    if A[mid] > mid:
        return mag_index_rec(A, left, mid - 1)
    else:
        return mag_index_rec(A, mid + 1, right)

#create wrapper function so user just needs to pass list and no other params
def mag_index(A):
    return mag_index_rec(A, 0, len(A) - 1)

print(mag_index(lst1))