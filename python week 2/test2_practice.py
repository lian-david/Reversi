#recursive function that converts a decimal number to binary
# example: if the input number is 66, the function should return 1000010

from unittest import result


def get_bin(num):
    if num == 0:
        return ""
    else:
        q = num // 2
        rem = num % 2
        return get_bin(q) + str(rem)

#print(get_bin(66))
#print(get_bin(10))

#another way, doesn't work:
# def dec_to_bin(num):
#     if num == 0:
#         return result
#     else:
#         result += num % 2 
#     return dec_to_bin(num / 2) + result

# print(dec_to_bin(66))

#function that gets a set of characters and a maximumlength
# returns a list of all the possible passwords that can be generated from the
# given characters up to the maximum length (repetitions are allowed).
#For example, generate_passwords(’abc’, 2) should return
#[’a’, ’b’, ’c’, ’aa’, ’ab’, ’ac’, ’ba’, ’bb’, ’bc’, ’ca’, ’cb’, ’cc’].

def generate_passwords(chars, pass_len):
    result = []
    if pass_len == 0:
        return result 
    if pass_len == 1:
        for ch in chars:
            result.append(ch)
    else:
        for ch in chars:
            for pwords in generate_passwords(chars, pass_len - 1):
                result.append(ch)
                result.append(ch + pwords)
    return set(result)

#print(generate_passwords("abc", 2))

def num_chocolate(money, price, wrap):
    choco = money / price
    return choco + num_wraps(choco, wrap)

def num_wraps(choco, wrap):
    if choco < wrap:
        return 0
    else:
        total = choco / wrap
    return int(total + num_wraps(total + choco % wrap, wrap))

#print(num_chocolate(16, 2, 2))
#print(num_chocolate(15, 1, 3))

#power of number
def get_power(num, exp):
    if exp == 0:
        return 1
    return num *(get_power(num, exp-1))

#print(get_power(2, 3))

#least common multiple
def get_LCM(n, m):
    total = n % m
    if total == 0:
        return n
    
    return n * get_LCM(m, total) / total

#print(get_LCM(2, 5))

#pascals triangle
def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        prev_line = pascal(n-1)
        for num in range(len(prev_line) - 1):
            line.append(prev_line[num] + prev_line[num + 1])
        line += [1]
    return line

#print(pascal(6))

def reverse_string(s):
    if s == "":
        return s

    return s[-1] + reverse_string(s[:-1]) 

print(reverse_string("the simple engineer")) 