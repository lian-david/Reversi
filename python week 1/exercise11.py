#sum of digits from input
num = int(input("Enter a number: "))

total = 0
while num > 0:
    digit = num % 10
    total += digit
    num = num // 10

print("Sum of digits:", total)
