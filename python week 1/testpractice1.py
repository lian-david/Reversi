#Given two integers return their product only if product is equal to or lower than 1000, else return their sum.

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# product = num1 * num2
# if product <= 1000:
#     print("The product of the numbers is:", product)
# else:
#     sum = num1 + num2
#     print("The sum of the numbers is:", sum)

#iterate the first 10 numbers and in each iteration print the sum of the current and previous number
previous_num = 0

for num in range(11):
    sum = num + previous_num
    print(f"Current number {num} Previous Number {previous_num} Sum: {sum}")
    previous_num = num
