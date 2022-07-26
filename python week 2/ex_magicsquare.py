#correct way to do magic square
size = int(input("Enter size of the square: "))

#mat = [[0] * size] * size      #doesn't work bc/ all rows point to same list in memory
#mat = [[0]* size for i in range (size)]    #list comprehension


#logic of list comprehension
#allocate the matrix
mat = []
for i in range(size):
    mat.append([0] * size)

#get the matrix from the user
for i in range(size):
    row = input(f"Enter row {i + 1}: ")
    numbers = row.split()
    for j in range(size):
        mat[i][j] = int(numbers[j])

is_magic_square = True

#check that the matrix contains all unique numbers between 1 and size^2
lst = [mat[i][j] for i in range(size) for j in range(size)]
lst.sort()
if lst != list(range(1, size**2 + 1)):
    is_magic_square = False

#check the rows
if is_magic_square:
    magic_num = sum(mat[0])

    for i in range(1, size):
        if sum(mat[i]) != magic_num:
            is_magic_square = False
            break 

#check the columns
if is_magic_square:
    for i in range(size):
        col = [mat[i][j] for i in range(size)]
        if sum(col) != magic_num:
            is_magic_square = False
            break

#check the diagonals
if is_magic_square:
    main_diag = [mat[i][i] for i in range(size)]
    if sum(main_diag) != magic_num:
        is_magic_square = False
    else:
        secondary_diag = [mat[i][size - i - 1] for i in range(size)]
        if sum(secondary_diag) != magic_num:
            is_magic_square = False

if is_magic_square:
    print("This is a magic square!")
else:
    print("This is not a magic square.")
