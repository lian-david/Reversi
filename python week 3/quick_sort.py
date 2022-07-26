#choose an element p from the array as the pivot
# pivot is the last element of the input list 
#partition the array A into 3 parts: A[0…k-1], A[k], and A[k+1…n-1]

def quicksort(A, left , right):
    #find pivot so that list is sorted smaller < pivot < greater 
    if left < right:
        pivot_idx = partition(A, left, right)
        quicksort(A, left, pivot_idx - 1)
        quicksort(A, pivot_idx + 1, right)

def partition(A, left , right):
    #last element is pivot
    pivot = A[right]
    #larger element index
    i = left - 1
    #compare each element to pivot
    for j in range(left, right):
        #if element j is smaller than pivot swap j w/ i
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[right] = A[right], A[i + 1]
    #return index of the pivot 
    return i + 1

lst = [4, 8, 2, 10, 5, 6, 3]
quicksort(lst, 0, len(lst) - 1)
print(lst)