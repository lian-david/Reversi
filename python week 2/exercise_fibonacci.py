#get positive int from user & print n numbers in fibonacci sequence
#this doesn't work
n = int(input("Enter a number to find the Fibonacci sequence: "))

d1 = 0
d2 = 1

print(d1, end = ' ')
for i in range(n - 1):
    print(d2, end = ' ')
    d = d2 + d1
    d1 = d2
    d2 = d
    