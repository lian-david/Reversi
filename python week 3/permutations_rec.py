#function that gets a string of unique characters and returns a list of all the
# permutations of the string

# def permutation(P):
#     if len(P) == 1:
#         return P

#     result = []

#     perms = permutation(P[1:])

#     for i, char in enumerate(P):
#         for perm in permutation(P[:i] + P[i+1:]):
#             result += [char + perm]
        
#     return result
    


# print(permutation("abc"))

#another way,correction:

def permutations(s):
    """Returns all permutations of a given string s

    Args:
        s(str): input string
    """
    if s == "":
        return [""]
    
    lst = permutations(s[1:])       #returns list of all permutations of s without first char
    result = []

    #go over all the permutations
    for perm in lst:
        #add the first char to every possible location in perm
        for i in range(len(s)):
            new_perm = perm[:i] + s[0] + perm[i:]
            result.append(new_perm)
            
    return result

# print(permutations("abc"))

#another way: 

def permutations2(s):
    if s == "":
        return [""]

    results = []

    #for every character c in s, find all the permutations of the string without c
    for i in range(len(s)):
        substring = s[:i] + s[i + 1:]
        # lst = permutations2(substring)  #list of permutations of substring
        # for perm in lst:                #add c to all perms 
        #     results.append(s[i] + perm)

        #using list comp:
        results += [s[i] + perm for perm in permutations2(substring)]

    return results

print(permutations2("abc"))    