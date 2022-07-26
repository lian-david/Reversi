#function that gets a matrix of integers M (represented by a two-dimensional 
# list), and returns the index of the row that has the maximum unique elements. 
# If there are multiple rows possible, return the minimum indexed row.

def is_unique(M):
    elem_counter = []
    for row in M:
        unique = set(row)
        elem_counter.append(len(unique))

    max_element = max(elem_counter)
    for lst in range(0, len(elem_counter)):
        if elem_counter[lst] == max_element:
            return lst

    # another way:
    #max_val = 0
    #max_index = 0
    #for i in range(0, len(M)):
        #count_unique = len(set(M[i]))
        #if count_unique > max_val:
            #max_val = count_unique
            #max_index = i
    #return max_index

print(is_unique([[1, 2, 2, 4], [2, 0, 4, 3], [1, 3, 1, 3]]))