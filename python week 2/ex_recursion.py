#recursive function that gets a positive integer n and prints all the integers
#from 1 until n

def numbers(n):
    if n == 1:
        print(n)
    else:
        #assume that print_numbers(n-1) already prints 1,...,n-1
        numbers(n-1)
        print(n)

numbers(4)

#recursive function that gets a string and returns its reverse

def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]

print(reverse_string("words"))

#another way

def reverse(s):
    if s == "":
        return s

    return reverse(s[1:]) + s[0]

print(reverse("abcde"))

def reverse2(s):
    if s == "":
        return s
    
    return s[-1] + reverse2(s[:-1])

print(reverse2("lian"))

#recursive function to compute the GCD (greatest common divisor) of two numbers

def GCD(m, n):
    if m >= n:
        return m%n
    else:
        return GCD(n, m % n)

print(GCD(24, 18))

#another way
def gcd2(m, n):     #gcd(24, 18) = gcd(18, 6) = gcd(6, 0) = 6
                    #gcd(15, 4) = gcd(4, 3) = gcd(3, 1) = gcd(1, 0) = 1
    #if second number is 0 then return first number bc there is no divisor
    #1 is gcd of any 2 numbers that don't have other divisors 
    if n == 0:
        return m
    return gcd2(n, m % n)

print(gcd2(25, 10))
print(gcd2(33, 3))