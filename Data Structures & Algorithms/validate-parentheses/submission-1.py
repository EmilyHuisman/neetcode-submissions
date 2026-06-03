class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        parenthDict = {"}": "{", "]":"[", ")": "("}

        for c in s:
            if c in parenthDict:
                if stack and parenthDict[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack


