#slice string to produce substrings 
s = "seehemewe"

#return see
print(s[0:3])
#return he
print(s[3:5])
#return me
print(s[5:7])
#return we
print(s[7:])
#return hem
print(s[3:6])
#return meh
print(s[5:2:-1])
#return wee
print(s[7::-3]) #alternatively s[-2::-3]