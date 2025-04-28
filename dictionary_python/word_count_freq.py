# Count Word Frequency
# Define a function to count the frequency of words in a given list of words.

# Example:

# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
# count_word_frequency(words) 
# Output:

#  {'apple': 3, 'orange': 2, 'banana': 1}

def count_word_frequency(words):
    my_dict = {}
    for ele in words:
        if my_dict.get(ele) is not None:
             my_dict[ele] += 1
        else:
            my_dict[ele] = 1
    return my_dict

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
print(count_word_frequency(words))
