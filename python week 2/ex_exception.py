#program that gets two integers from the user and prints their sum
#program should keep asking the user for input until they enter a valid one

def get_int(prompt="Enter a number:"):
    while True:
        try: 
            num = int(input(prompt))
            return num 
        except ValueError:
            print("Input must be numeric. Try again.")

num1 = get_int("Enter the first number: ")
num2 = get_int("Enter the second number: ")
print(num1 + num2)
