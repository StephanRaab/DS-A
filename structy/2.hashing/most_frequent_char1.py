from collections import Counter

# most frequent char
# Write a function, most_frequent_char, that takes in a string as an argument. 
# The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

# You can assume that the input string is non-empty.

def most_frequent_char(s):
  most_frequent_num  = 0
  most_frequent_char = None
  count = Counter(s)

  print(count)
  
  for char in count:
    if count[char] > most_frequent_num:
      most_frequent_num = count[char]
      most_frequent_char = char

  return most_frequent_char

most_frequent_char('bookeeper') # -> 'e'
most_frequent_char('david') # -> 'd'
most_frequent_char('mississippi') # -> 'i'
