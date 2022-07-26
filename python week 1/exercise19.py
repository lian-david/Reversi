#get list of numbers from user, remove duplicates from list, print w/o duplicates
num = input("Enter a list of numbers: ")
numbers = num.split()

no_dupes = set(numbers)
print(no_dupes)