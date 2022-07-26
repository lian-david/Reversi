#function that gets a list of ints and an integer K
#finds a pair of elements in the list whose sum is equal to K

# def get_sum(nums, K):
#     """This function computes the sum of elements in list that equal K

#     Args:
#         nums(list): The input list
#         K(int): The input number
#     Returns:
#         The sum of two elements equal to K
#     """

#     result = []

#     for i in nums:
#         for j in nums:
#             if i + j == K:
#                 result.append(i)

#     return result

# print(get_sum([1, 5, 1, 7, 2, 3], 7))

#correction

def find_sum(lst, K):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == K:
                return lst[i], lst[j]
    return None

lst = [3, 8, 4, 6, 10, 9]
print(find_sum(lst, 14))
print(find_sum(lst, 50))

#better way
def find_sum2(lst, K):
    s = set()
    for num in lst:
        #search for the complement of num in the set
        if K - num in s:
            return num, K - num
        s.add(num)

    return None
