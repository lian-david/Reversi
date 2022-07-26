#function that given a list of the available denominations, determine if it's
#possible to receive exact change for an amount of money

def change(denominations, target_money):
    if target_money <= min(denominations) and target_money == 0:
        return True
    if target_money <= min(denominations) and target_money != 0:
        return False
    else:
        return target_money - change(denominations[0:])

# print(change([4, 17, 29], 75))
# print(change([5, 10, 25, 100, 200], 94))

#correction:

def has_exact_change(lst, target):
    """Checks if we can get to the exact target money using the denominations
    Args: 
        lst(list): list of denominations
        target(int): the target money
    """
    if target == 0:
        return True
    if target < 0:
        return False

    for d in lst:
        if has_exact_change(lst, target - d):
            return True
    return False

print(has_exact_change([4, 17, 29], 75))
print(has_exact_change([5, 10, 25, 100, 200], 94))