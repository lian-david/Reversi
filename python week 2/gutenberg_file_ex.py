import string
import math

# def frequent_words(file_path):
#     word_dict = {}
#     lines = ""

#     with open(file_path, "r", encoding="UTF-8") as f:
#         for line in f:
#             lines = [ch for ch in line if ch not in string.punctuation]
#             lines = "".join(lines)
#             lines = lines.split()
#             for word in lines:
#                 word = word.lower()
#                 if word in word_dict:
#                     word_dict[word] += 1
#                 else:
#                     word_dict[word] = 1

#         words_tuple = tuple(word_dict.items())
#         sorted_words = sorted(words_tuple, key=lambda s:s[1], reverse=True)
        
#     return sorted_words

# def frequency_word_list(file_path, n_words):
#     word_frequencies = frequent_words(file_path)

#     for word in range(0, n_words + 1):
#         print(word_frequencies[word][0], ":", word_frequencies[word][1])
        


# def zipf_law(file_path, n_words=100):
#     word_list = frequent_words(file_path)
#     number_one_word = word_list[0][1]
#     number_one_log = (math.log(number_one_word))
#     rank = 1
    
#     for word in range(0, n_words + 1):
#         predict = (((number_one_log) - (math.log(rank))))
#         print("Number of occurrences:",word_list[word][1], "Predicted occurrences:", predict)
#         rank+=1
 
# zipf_law("gutenberg.txt")
# #frequency_word_list("gutenberg.txt",100)

#correction

def get_most_frequent_words(file_path, n_words=100, encoding="utf-8"):
    """This function finds the most frequent words in the given file. 

    Args:
        file_path
        n_words(int): defaults to 100
        encoding(str): defaults to "utf-8"
    
    Returns:
        A list of tuples [(w1, freq1), (w2, freq2),...]
    """
    word_counts = {}    #key = words, values = counts

    with open(file_path, encoding=encoding) as f:
        for line in f:
            clean_line = "".join([ch for ch in line if ch not in string.punctuation])
            words = clean_line.lower().split()

            #update the word counts
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1 
                else:
                    word_counts[word] = 1

    #sort the words by their frequency in decreasing order 
    sorted_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_counts[:n_words]

def zipf_law_prediction(rank, C, a=1):
    return math.exp(math.log(C) - a * math.log(rank))

most_frequent_words = get_most_frequent_words("gutenberg.txt")
C = most_frequent_words[0][1]

rank = 1
for word, count in most_frequent_words:
    predicted_count = zipf_law_prediction(rank, C)
    print(word, count, round(predicted_count, 2))
    rank +=1

