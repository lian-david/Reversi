#put user sentence in alphabetical order then sort for first letter a

sent = input("Enter a sentence: ")
lst = sent.split()
lst.sort()

for i in lst:
    if i.startswith("a") == True:
        lst[0] = i
    break 
print(lst)

#another way, returns number of words that start with a 
#starts_with_a = 0
#for i in lst:
#if i[0] == "a":
#starts_with_a +=1
