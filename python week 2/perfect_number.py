#Write a function that gets a number & returns whether its a perfect number or not

def perfect_number(num):
    """ Function returns T/F for given integer depending on if its a perfect number

    Args:
        num(int): A given integer
    Returns:
        True/False
    """
    total = 0
    for i in range(1,num):
        if num % i == 0: 
            total += i
    if total == num:
        return True
    else:
        return False

print(perfect_number(496))

#Based on the function from the previous part, write a function that gets a number
#n and returns a list of all the perfect numbers that are less than or equal to n.

def perfect_nums(n):
    """ Function returns list of all perfect numbers less than or equal to given number

    Args:
        n(int): A given integer
    Returns:
        small_nums(list): List of all perfect numbers smaller than given integer
    """
    small_nums = []
    for num in range(1, n):
        total = 0
        for i in range(1, num):
            if num % i == 0: 
                total += i 
        if total == num:
            small_nums.append(num)
    return small_nums

print(perfect_nums(10000))

#correction
def is_perfect(num):
    """This function checks if the number is perfect (equal to sum of its divisors)

    Args:
        num(int): the given number
    """
    divisors_sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors_sum += i

    return num == divisors_sum      #no need for if statement bc this condition is already T/F

print(is_perfect(28))

def get_perfect_numbers(n):
    """ Return a list with all the perfect numbers <= n
    
    Args:
        n(int): upper limit of the seach range 
    """
    lst = []
    for i in range(2, n  + 1):
        if is_perfect(i):
            lst.append(i)

    #lst comprehension for same thing:
    #return[i for i in range(2, n+1) if is_perfect(i)]

    return lst

print(get_perfect_numbers(10000))