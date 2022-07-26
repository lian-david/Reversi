#recursive function that computes the power an for any real number a and an integer n
#If n is even, then a^n = (a^n/2)^2
#If n is odd, then a^n = a(a^(n-1)/2)^2

def power(a, n):
    if n == 0:
        return 1
    
    if n % 2 == 0:
        n //= 2
        return power(a, n) ** 2
    else:
        return a * power(a, (n-1) // 2) ** 2

    

print(power(2, 2))
print(power(2, 3))
print(power(2, 4))
print(power(3, 4))

#correction:
def powers(a, n):
    if n == 0:
        return 1
    
    if n % 2 == 0:
        return powers(a, n//2) ** 2
    else:
        return a * powers(a, (n-1) // 2) ** 2

print(powers(3, 4))