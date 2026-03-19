# https://leetcode.com/problems/valid-palindrome/submissions/1953094854/
def isPalindrome(self, s: str) -> bool:
    length = len(s)
    left = 0
    right = length -1

    while left < right:
        print(left, right)

        if not s[left].isalnum():
            left += 1
            continue

        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False


        left += 1
        right -= 1
    
    return True