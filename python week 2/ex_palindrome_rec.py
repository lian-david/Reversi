#recursive function that gets a string and returns True if it is a palindrome

def is_palindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("radar"))
print(is_palindrome("racecar"))
print(is_palindrome("not"))