# intersection

# Write a function, intersection, that takes in two lists, a,b, as arguments.
# The function should return a new list containing elements that are in both of the two lists.

# You may assume that each input list does not contain duplicate elements.

def intersection(a, b):
  adict = {}
  res = []
  for index, num in enumerate(a):
    adict[num] = index

  for num in b:
    if num in adict:
      res.append(num)

  return res

intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
intersection([4,2,1], [1,2,4,6]) # -> [1,2,4]
intersection([0,1,2], [10,11]) # -> []