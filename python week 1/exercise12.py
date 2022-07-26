#construct a pattern

for i in range(1,10):
    print(str(i)*i, end = "\n")
    

#correct way with nested loop
# for i in range(1,10):
#     for j in range(i):
#         print(i, end = " ")
#     print()