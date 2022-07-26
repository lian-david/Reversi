#There are n stairs, a person standing at the bottom wants to reach the top
# The person can climb either 1 stair or 2 stairs at a time
#function that returns the number of ways the person can reach the top

#not correct
def stairs(n):
    ways = []
    if n == 1: 
        ways.append([1])
        return ways
    if n == 2:
        ways.append([1, 2])
        return ways
    
    return stairs(n - 1) + stairs(n - 2)
    
        
print(stairs(4))

#correction 

def find_ways_to_climb(n):
    """This function finds in how many ways you can climb n stairs, using 1 or 2 stairs

    Args:
        n(int): Given number
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    return find_ways_to_climb(n-1) + find_ways_to_climb(n-2)

print(find_ways_to_climb(4))


#Now change the function to also return the ways themselves

#correction, i don't think this works well

def climb_stairs(n):
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1, 1], [2]]

    result = []
    lst = climb_stairs(n-1)     #list with all ways to climb n-1 stairs 
    #add the last step of 1 to each way of climbing n-1 stairs 
    for way in lst:
        result.append(way + [1])

    lst2 = climb_stairs(n-2)     #list with all ways to climb n-2 stairs
    #add the last step of 2 to each way of climbing n-2 stairs 
    for way in lst2:
        result.append(way + [2])

    return result

print(climb_stairs(3))

#another way for correction with list comp

def climb_stairs2(n):   #format of result [ [], [], [] ]
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1, 1], [2]]

    result = [way + [1] for way in climb_stairs2(n-1)]
    result += [way + [2] for way in climb_stairs2(n-2)]

    return result

print(climb_stairs2(3))