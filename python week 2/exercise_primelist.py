#sieve of erathostenes, still don't understand mathematical logic 
import math

# num = int(input("Enter a number: "))

# prime_lst = [True for i in range(num+1)]
# p = 2

# while(p*p <= num):
#     if prime_lst[p] == True:
#         for i in range(p*p, num+1, p):
#             prime_lst[i] = False
#     p +=1

# for p in range(2, num+1):
#     if prime_lst[p]:
#         print(p)

# lst = [i for i in range(2, num+1)]
# p = 2
# for i in lst:

#another way

num = int(input("Enter upper limit for searching primes: "))

#initially mark all the numbers in the range as primes
primes = [True] * (num + 1)
upper = int(math.sqrt(num)) + 1

#go over all the numbers in the range and mark their multiples as non-primes
for p in range(2, upper):
    if primes[p]:
        #mark all the multiples of p as non-prime
        for m in range(p**2, num + 1, p):
            primes[m] = False

for i in range(2, num + 1):
    if primes[i]:
        print(i, end =" ")
