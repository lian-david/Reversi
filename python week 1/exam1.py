#Question 1:

# numbers = input("Enter a list of numbers (separated by space): ")
# numbers = [int(num) for num in numbers.split()]

# min = int("inf")
# second_min = float("inf")

# for num in numbers: 
#     if num < min:
#         second_min = min        
#         min = num
#     elif num < second_min:
#         second_min = min

# print("The second smallest numbers is: ", second_min)

#Question 2:

# s = input("Enter a string: ")
# count_chars = {}

# for ch in s:
#     if ch in count_chars:
#         count_chars[ch] +=1
#     else:
#         count_chars[ch] = 1

# max_count = max(count_chars.values())
# max_occurring_chars = [ch for ch in count_chars[ch] == max_count]
# print(max_occurring_chars)

#Question 3
mat = [[-1, 4, 6, 7], [0, 6, 10, 14], [3, 10, 21, 25], [4, 14, 52, 60]]

is_sorted = True
#check that rows are sorted 
for row in mat:
    for j in range(len(row) - 1):
        if row[j] > row[j + 1]:
            is_sorted = False
            break 

    if not is_sorted:
        break 

#check that the columns are sorted 
if is_sorted:
    for j in range(len(mat[0])):
        #get the numbers of column number j
        column = [mat[i][j] for i in range(len(mat))]

        #check that the column is sorted by comparing each element to the next one
        for i in range(len(mat) - 1):
            if column[i] > column[i + 1]:
                is_sorted = False
                break
        if not is_sorted:
            break
if is_sorted:
    print("The matrix is sorted!")
else:
    print("The matrix is not sorted.")