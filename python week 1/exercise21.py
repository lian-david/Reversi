#write a function to calculate the factorial of a number 

#didnt finish in time
# def get_factorial(num):
#     if num < 0:
#         print("This number can not be used for factorial.")
#     elif num = 0:
#         print("The factorial of the number is 1.")
#     else: 
#         n = 1
#         for i in range(1, num+1):
#         n = n * i
#     return n

#correction
def factorial(num):
    """This function computes the factorial of a given number.

    Args: 
        num(int): The input number
    Returns:
        The factorial
    """
    #don't need to account for 0 & 1 factorial bc/ loop won't run and result will return 1

    if num < 0:
        print("Invalid input")
        return  #want to return immediately and rest of function wont run 

    result = 1
    for i in range(2, num + 1):
        result *= i

    return result

print(factorial(6))
print(factorial(0))
print(factorial(20))
