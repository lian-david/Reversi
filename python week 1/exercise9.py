#get string from user and print whether its a palindrome, pal ex: level, radar
word = input("Enter a word: ")
is_palindrome = (word == word[::-1])
print("Is the word a palindrome? ", is_palindrome)