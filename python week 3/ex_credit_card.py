#function that takes a credit card number as a string of digits (in four groups,
# separated by spaces) and establishes if it is valid or not.

def is_valid(card_num):
    card_num = card_num.replace(" ", "")
    reverse_num = card_num[::-1]
    digit_sum = 0

    #if digit is at odd index, double the value
    for num in range(len(reverse_num)):
        if num % 2 == 0:
            digit_sum += int(reverse_num[num])
        else:
            double_num = 2 * int(reverse_num[num])
            if double_num > 10:
                digit = double_num % 10
                digit2 = double_num // 10
                double_num = digit + digit2
            digit_sum += double_num
    
    if digit_sum % 10 == 0:
        return True
    else:
        return False
        
        
print(is_valid("4799 2739 8713 6272"))
print(is_valid("4799 2739 8713 6282"))
