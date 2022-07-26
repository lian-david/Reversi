#recursive function that returns the power set of a given set
#power set = all subsets of the set 

def power_set(lst):
    result = [[]]
    if len(result) == 0:
        return result
 
    for n in lst:
        result.append([n])
        if power_set(lst[:-1]):
            result.append(n) 
            
    return result
        

print(power_set([1, 2, 3]))

# correction
def power_set2(A):
    if len(A) == 0:
        return [[]]
    
    result = []
    S = power_set2(A[1:])  #returns the power set of A without the first element
    # for subset in S:
    #     result.append(subset)
    #     result.append([A[0]] + subset)
    # return result

    #another way with list comp:
    S += [[A[0]] + subset for subset in S]
    return S

#print(power_set2([1, 2, 3]))

