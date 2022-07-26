#sum all the numbers that divide by 7 between 100 & 200

total = 0 
for i in range (100, 201):
    if i % 7 == 0: 
        total += i
print("The sum is:", total)
