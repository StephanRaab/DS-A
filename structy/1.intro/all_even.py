# all even
# Write a function, all_even, that takes in a list of numbers as an argument. 
# The function should return a boolean indicating whether or not every element of the list is an even number.

def all_even(nums):
    for num in nums:
        if num % 2 == 1:
            return False
    
    return True

all_even([4, 90, 68, 6, -2]) # -> True