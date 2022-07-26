#Write a function that gets a list of words and returns their longest common prefix

def longest_prefix(word_lst):
    '''Function returns longest common prefix for words in a given list

    Args:
        word_lst(list): Given list of words
    Returns: 
        pre(str): String of common prefix of words
    '''
    if len(word_lst) == 1:
        return word_lst[0]

    word_lst.sort()
    pre = ""
    shortest_word = word_lst[0]

    for ch in range(len(shortest_word)):
        if word_lst[len(word_lst)- 1][ch] == shortest_word[ch]:
            pre += word_lst[len(word_lst) - 1][ch]
        else:
            break

    return pre

print(longest_prefix(["undo", "uncouple", "university"]))
print(longest_prefix(["undo", "uncouple", "university", "red"]))
print(longest_prefix(["can", "cannot", "candid"]))

#correction
def longest_common_prefix(words):
    #min(words, key = len)   #finds smallest string based on length key
    shortest_word_len = len(min(words, key = len))  #want length of shortest word
    longest_prefix = ""

    #go over all the characters
    for i in range(shortest_word_len):
        #get the i character of the first word 
        curr_char = words[0][i]

        #go over all the words 
        for j in range(1, len(words)):
            #compare the i character of the j word to the i character of first word
            if words[j][i] != curr_char:
                return longest_prefix

        longest_prefix += curr_char
    return longest_prefix

print(longest_common_prefix(["undo", "uncouple", "university"]))