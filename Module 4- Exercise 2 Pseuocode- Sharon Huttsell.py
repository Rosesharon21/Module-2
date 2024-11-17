import random

def open_random_page(dictionary):
    return random.choice(dictionary)

def lookup_word(dictionary, target_word):
    current_page_word = open_random_page(dictionary)
    while current_page_word != target_word:
        if current_page_word < target_word:
            # Flip forward
            current_page_word = dictionary[min(dictionary.index(current_page_word) + 1, len(dictionary) - 1)]
        else:
            # Flip backward
            current_page_word = dictionary[max(dictionary.index(current_page_word) - 1, 0)]
    return f"Found the word: {target_word}"

# Example dictionary (sorted list of words)
dictionary = ["apple", "banana", "juice", "lamb", "logic", "monkey", "zebra"]

# Target word to look up
target_word = "logic"

# Perform the lookup
result = lookup_word(dictionary, target_word)
print(result)
