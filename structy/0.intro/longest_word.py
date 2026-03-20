# longest word
# Write a function, longest_word, that takes in a sentence string as an argument. The function should return the longest word in the sentence. 
# If there is a tie, return the word that occurs later in the sentence.

def longest_word(sentence):
    split = sentence.split(" ")
    longest = ""

    for word in split:
        if len(word) > len(longest):
            longest = word

    return longest

longest_word("what a wonderful world") # -> "wonderful"