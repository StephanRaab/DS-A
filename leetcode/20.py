class Solution:
    def isValid(self, s: str) -> bool:
        d = {")":"(", "}":"{", "]":"["}
        stack = []

        if len(s)%2 != 0:
            return False

        for c in s:
            if c in d:
                if stack and d[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False