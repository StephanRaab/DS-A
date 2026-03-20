# max value
# Write a function, max_value, that takes in list of numbers as an argument. The function should return the largest number in the list.
def max_value(nums):
    res = float("-inf")

    for num in nums:
        if num > res:
            res = num

    return res

max_value([4, 7, 2, 8, 10, 9]) # -> 10