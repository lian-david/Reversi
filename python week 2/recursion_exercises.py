#function gets a set of characters and a maximum length, and returns a list of 
# all possible passwords that can be generated from the 
# given characters up to the maximum length


#recursive function that converts a decimal number to binary
# example: if the input number is 66, the function should return 1000010

def get_bin(number):
    if number == 0:
        return bin(number)

    for num in range(number):
        return bin(number)[2:]

    return get_bin(number - 1)

print(get_bin(66))
print(get_bin(10))


#program to get the sum of a non-negative integer
def sum_nums(nums):
    if nums == 0:
        return 0
    else:
        return nums % 10 + sum_nums(int(nums / 10))

#print(sum_nums(345))

#program to calculate the value of 'a' to the power 'b'
def powers(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a 
    else:
        return a * powers(a, (b-1))

#print(powers(3,4))

#factorial
def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n - 1)

#print(factorial(5))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#print(fibonacci(10))

#check if a number is palindrome, this is wrong
def num_palindrome(n):
    n = str(n).split()
    if len(n) < 2:
        return True
    if n[0] != n[-1]:
        return False
    
    return num_palindrome(n[1:-1])

print(num_palindrome(555))
print(num_palindrome(1451))

