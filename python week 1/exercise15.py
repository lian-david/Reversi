#list comprehension
lst = [x for x in range(7, 100, 7) if x % 3 ==0]
print(lst)

#find all of the words in a string that have less than 5 letters
s = "an apple a day keeps the doctor away"
short_words = [word for word in s.split() if len(word) < 5]
print(short_words)

#remove all the vowels from a given string
VOWELS = "aeiou"
s_without_vowels = [letter for letter in s if letter not in VOWELS]
print("".join(s_without_vowels))
