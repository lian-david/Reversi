#check if number is prime

# n = int(input("Enter a number to see if it is prime: "))

# is_prime = True

# for i in range(2,n):
#     if n == 1:
#         is_prime = False
#     elif (n % i) == 0:
#         is_prime = False
# print("{} is prime.".format(n), is_prime)

#correct way
num = int(input("Enter a number: "))

is_prime = True 
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print("The number is prime.")
else:
    print("The number is not prime.")