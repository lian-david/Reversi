#function that gets a list of numbers, and finds any three numbers which sum to zero

#simplest solution, time complexity = O(n^3)
def find_triplet_zero(lst):
    for i in range(len(lst)-2):
        for j in range(i+1, len(lst)-1):
            for k in range(j + 1, len(lst)):
                if lst[i] + lst[j] + lst[k] == 0:
                    return [lst[i], lst[j], lst[k]]
    return None

#print(find_triplet_zero([3, 5, 8, 10, -9, -11]))

#more efficient way, time complexity = O(n^2)
#space complexity = O(n)
def find_triplet(lst):
    for i in range(len(lst) - 2):
        #search for a pair of numbers equal to -lst[i]
        s = set()
        for j in range(i+1, len(lst)):
            #check whether we have a number x in the set that together with lst[j] will give us -lst[i]
            x = -(lst[i] + lst[j])
            if x in s:
                return [x, lst[i], lst[j]]
            else:
                s.add(lst[j])
    return None

#print(find_triplet([3, 5, 8, 10, -9, -11]))

#better solution, time complexity = O(n logn) + O(n^2) = O(n^2)
#space complexity: depends on sorting algorithm unless algorithm sorts in place 
#                   (this one doesnt), in the best case O(1)
def find_triplet_zero2(lst):
    lst = sorted(lst)
    for i in range(len(lst) - 2):
        #find a pair of numbers equal to -lst[i] in the rest of the list
        left = i + 1
        right = len(lst) - 1 
        
        while left < right:
            total = lst[left] + lst[right] + lst[i]
            if total == 0:
                return [lst[left], lst[right], lst[i]]
            elif total > 0:
                right -= 1
            else:
                left += 1

    return None

print(find_triplet_zero2([3, 5, 8, 10, -9, -11]))