#function that gets list of points (each point is a tuple of (x, y)) and 
# returns the points sorted by their Euclidean distance from the origin (0, 0)

#for math purposes: this is not euclidean distance, it is euclidean squared 

def sort_by_distance(points):
    return sorted(points, key=lambda p: p[0]**2 + p[1]**2)     #this is x squared + y squared

points = [(2,5), (3,8), (1,1), (-1,1), (0,5)]
print(sort_by_distance(points))

#function that gets a list of strings and returns the longest string in the list

# words = ["cat", "passed", "house"]
# result2 = max(words, key=len)
# print(result2)

def get_longest_string(strings):
    return max(strings, key=len)

strings = ["some", "string", "another"]
print(get_longest_string(strings))

