def anagrams(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)

    is_anagram = False

    if len(s1) == len(s2):
        if(s1 == s2):
            is_anagram = True
    else:
        is_anagram = False

    if is_anagram:
        print("The words are anagrams!")
    else:
        print("The words are not anagrams.")

#anagrams("cheaters", "teachers")
#anagrams("no", "yes")

#correction:
def are_anagrams(str1, str2):
    return count_letters(str1) == count_letters(str2)

def count_letters(s):
    """Get a string and count how many times each letter appears in the string

    Args:
        s(str): given string
    Returns:
        A dictionary of (letter, count)
    """
    counts = {}
    for letter in s:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts

#print(are_anagrams("cheaters", "teachers"))
#print(are_anagrams("hello", "world"))

# def get_bin(n):
#     if n == 0:
#         return ""

#     result = []
    
#     for num in range(0, n+1):
#         print(result[num], end="")

#     result[num] = 0
#     get_bin(n + 1)
#     result[num] = 1
#     get_bin(n)
    
#print(get_bin(3))

#correction:
def binary_strings(n):
    """Returns all the binary strings of length n
    Args:
        n(int): length 
    """
    if n == 0:
        return [""]

    lst = binary_strings(n-1)     #returns all the binary strings of length n-1
                                  #e.g : for n = 3, we get ["00", "01", "10", "11"]
    # result = []
    # for s in lst:
    #     result.append(s + "0")
    #     result.append(s+ "1")
    # return result

    #using list comprehension:
    result = [s + "0" for s in lst]
    result += [s + "1" for s in lst]
    return result

#print(binary_strings(4))

def get_grades(source_file, dest_file, encoding="utf-8"):
    with open(source_file, "r") as grades, open(dest_file, "w") as final:
        b = grades.readline()
        while b:
            for line in grades:
                lst = line.split()
                avg = (((lst[-1]*0.4) + (lst[-2]*0.2) + ((lst[-3]+ lst[-4] + lst[-5] + lst[-6])*0.1)))
                final.write(lst[1][2], avg)

#get_grades("grades.txt", "final_grades.txt")

#correction:
def compute_final_grades(students_file= "grades.txt", 
                        final_grades_file="final_grades.txt",
                        weights = [0.1, 0.1, 0.1, 0.1, 0.2, 0.4]):
    try:
        student_grades = {}

        #read the data from the students file and stor the weighted average
        #of each student in a dictionary 
        with open(students_file) as f:
            for line in f:
                fields = line.split(", ")
                name = fields[0]
                grades_avg = 0
                for i in range(len(weights)):
                    grades_avg += weights[i] * int(fields[i+1])
                student_grades[name] = grades_avg

        #sort the dictionary using the names of the students 
        sorted_names = sorted(student_grades)

        #print the final grades to the output file
        with open(final_grades_file, "w") as f:
            for name in sorted_names:
                print(name, student_grades[name], sep=",", file=f)
    except Exception as e:
        print(e)
        
#compute_final_grades()