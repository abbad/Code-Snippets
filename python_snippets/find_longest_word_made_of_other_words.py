"""
 Find the longest word made of other words in a list.
"""

def print_longest(list_of_words):
    # Create a dictionary of the words.
    words_dict = {}
    for word in list_of_words:
        words_dict[word] = True

    # Sort descending.
    list_of_words.sort(key=lambda x: len(x), reverse=True)

    # Iterate over and return the longest word.
    for word in list_of_words:
        if can_build_word(words_dict, word, True):
            print(word)

def can_build_word(words_dict, word, is_original):
    # Check if word is in the dictionary and its not original.
    if word in words_dict.keys() and not is_original:
        return words_dict[word]

    # Split the word given and call the function recursively with different combination.
    for x in range(1, len(word)):
        right = word[0:x]
        left = word[x:]
        if left in words_dict and words_dict[left] is True and can_build_word(words_dict, right, False):
            return True

    # Add the word to the dictionary with flag equals to false so we know that we calcualted it before.
    # (Dynamic programming)
    words_dict[word] = False
    return False

if __name__ == '__main__':
    list_of_words = ['banana', 'cat', 'nana', 'dog', 'cat', 'walk', 'walker', 'dogwalkercat']
    print_longest(list_of_words)