#Get text from user & count number of occurrences of each word in text
import string

# sent = (input("Enter a sentence: "))
# lst = sent.split()

# num_words = {}

# for word in lst: 
#     if word not in num_words:
#         num_words[word] = 1
#     else:
#         num_words[word] += 1

# print(num_words)

#corrections
text = input("Enter a sentence: ")

#converting to list, removing punctuation from string, convert back to string
clean_text = "".join([ch for ch in text if ch not in string.punctuation])
words = clean_text.split()

word_counts = {}    #key = word, value = number of occurrences 

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

#print output in user friendly way, removing dictionary punctuation
for word, count in word_counts.items():
    print(word, count)
