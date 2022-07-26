import random as r

def get_range(lst, min_val, max_val):
    """ Returns all the items in the list in range between min_val and max_val

    Args:
        lst(list): List from user input
        min_val(int): Minimum value
        max_val(int): Maximum value
    Returns:
        lst2(list): Modified list of numbers in range 
    """
    lst2 = []
    for item in lst:
        if min_val <= item <= max_val:
            lst2.append(item)

    return lst2

    #another way
    #return [x for x in lst if min_val <= x <= max_val]

def get_random_item(lst):
    """Return a random item from the list

    Args:
        lst(list): List from user input
    Returns:
        item(list): Random item from list
    """
    item = r.choice(lst)
    return item

    #another way
    #idx = r.randint(0, len(lst) - 1)
    #return lst[idx]

def second_min(lst):
    """Returns the second smallest number in the list

    Args:
        lst(list): List from user input
    """
    new_lst = lst.sort()
    return new_lst[1]


