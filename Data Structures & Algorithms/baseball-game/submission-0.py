class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ans = 0
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
                ans += stack[-1]
            elif op == 'D':
                stack.append(2 * stack[-1])
                ans += (stack[-1])
            elif op == 'C':
                ans -= stack[-1]
                stack.pop()
            else:
                stack.append(int(op))
                ans += stack[-1]
        return ans