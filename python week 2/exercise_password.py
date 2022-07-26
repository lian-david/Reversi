# #check if user password is valid
# #one uppercase & one lowercase letter
# #one digit 0-9
# #min length 6 char, max length 16 char
# #one special character

# #this doesn't work
# pword = input("Enter a password: ")

# is_valid = False
# uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# lowercase = "abcdefghijklmnopqrstuvwxyz"
# digits = "0123456789"
# special_char = "!$#@%"

# if (len(pword) >= 6) and (len(pword) <= 16):
#     for i in pword:
#         if (i not in uppercase):
#             is_valid = False
#         if (i not in lowercase):
#             is_valid = False
#         if (i not in digits):
#             is_valid = False
#         if (i not in special_char):
#             is_valid = False

# if is_valid:
#     print("Password is valid.")
# else:
#     print("Password is not valid.")

#correct way 
password = input("Enter a password: ")

has_lower = False
has_upper = False
has_digit = False
has_special = False
is_valid = False

SPECIAL_SYMBOLS = "!$#@%"

if 6 <= len(password) <= 16:
    for ch in password:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif ch in SPECIAL_SYMBOLS:
            has_special = True
    
    is_valid = has_lower and has_upper and has_digit and has_special
else:
    is_valid = False

if is_valid:
    print("Password is valid.")
else:
    print("Password is not valid.")

