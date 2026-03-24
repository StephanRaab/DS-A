from collections import Counter

def anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

anagrams('monkeyswrite', 'newyorktimes') # -> True
anagrams('paper', 'reapa') # -> False
