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

def intersectionSet(a, b): 
  res = []
  items = set()

  for item in a:
    items.add(item)

  for num in b:
    if num in items:
      res.append(num)

  return res

def intersectionSet(a, b): 
  res = []
  items = set(a)

  for num in b:
    if num in items:
      res.append(num)

  return res  

def superShortIntersection(a,b):
    items = set(a)
    return [el for el in b if el in items]

intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
intersection([4,2,1], [1,2,4,6]) # -> [1,2,4]
intersection([0,1,2], [10,11]) # -> []

intersectionSet([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
intersectionSet([4,2,1], [1,2,4,6]) # -> [1,2,4]
intersectionSet([0,1,2], [10,11]) # -> []