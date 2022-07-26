s = str(input("Enter a small English letter (a-z): "))

#Use ord to find int, -32 for ascii number, chr to get letter from number
let = ord(s)
let = let - 32
let = chr(let)
print("The corresponding capital letter is:", let)

#alternative:
#gap = ord('a') - ord('A')
#capital = chr(ord(s) - gap)
#print(capital)