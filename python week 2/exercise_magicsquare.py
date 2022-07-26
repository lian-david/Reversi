#doesn't fully work
num = int(input("Enter number for magic square: "))

mat = [[0 for x in range(num)]
        for y in range(num)]

i = num // 2
j = num - 1

n = 1
while n <= (num**2):
    if i == -1 and j == num:
        j = num - 2
        i = 0
    else:
        if j == num:
            j = 0
        if i < 0:
            i = num - 1
    if mat[int(i)][int(j)]:
        j = j - 2
        i = i - 1
        continue
    else:
        mat[int(i)][int(j)] == n
        n = n + 1

    j = j + 1
    i = i - 1 

for i in range(0, num):
    for j in range(0, num):
        print(mat[i][j], end =' ')
        if j == num -1:
            print()


# for i in range(len(mat)):
#     #define length of columns 
#     for j in range(len(mat[i])): 
