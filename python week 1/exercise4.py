digits = int(input("Please enter a 3-digit number: "))

#Extracting 3 digits from the input one by one
temp = digits % 10
digits = digits // 10
rem = digits % 10
digits = digits // 10
total = digits

new_total = temp + rem + total
print("Sum of digits:", new_total)