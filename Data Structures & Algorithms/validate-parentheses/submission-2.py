class Solution:
    def isValid(self, s: str) -> bool:
        #8/05
        stack = []

        parDict = {"}": "{", "]":"[", ")": "("}

        for c in s:
            if c in parDict:
                if stack and parDict[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack




















        '''
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
        '''

