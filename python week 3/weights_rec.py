#function that gets a list of weights L, and a target weight w, and returns true 
# if it is possible to have some selection of weights from L that sum to w

def weights(L , w):
    if w == 0:
        return True
    if len(L) == 0:
        return False

    for weight in L:
        w -= weight
        if weights(L[1:], w):
            return True

    return False

    
    

print(weights([1, 4, 5, 6], 10))
print(weights([1, 4, 5, 6], 8))
print(weights([1, 4, 5, 6], 9))

