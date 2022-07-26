#get numbers from user until they enter -1 and store them in a list
#print average of numbers in the list 

lst = []
num = int(input("Enter a number (-1 for exit): "))

while num != -1:
    lst.append(num)
    num = int(input("Enter a number (-1 for exit): "))

total = 0
for num in lst:
    total += num

#avg = sum(lst)/len(lst)
print("The average of the list is:", total/len(lst))