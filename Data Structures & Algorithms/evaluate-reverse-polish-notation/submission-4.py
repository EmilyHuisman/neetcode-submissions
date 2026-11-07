class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''

        ["1","2","+","3","*","4","-"]
        ((1 + 2) * 3) - 4 = 5

        
        1 2 

        the value closest to the num is on the 

        1 2 3 x -
        
        1 - 2 x 3
        
        1 2 - 3 x
        (1 - 2) x 3

        [1 2]
        * when we reach an operand, pop last 2 values, then push back to stack

        have an operand hashmap
        loop thru tokens, pushing numbers to stacl
        when you reach an operand, take left and right vals and compute then push back to hashmap and cntue



        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        ["10","6",12,"-11","*","/","*","17","+","5","+"]


        [10, 6, 12, -11]
        ((10 * (6 / ((9 + 3) * -11))) + 17) + 5




       
        import operator
        stack = []
        operands = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        for num in tokens:
            if num not in operands:
                stack.append(int(num))
            else:
                right = stack.pop()
                left = stack.pop()
                calc = operands[num]
                val = calc(left, right)
                if operands == "/":
                    math.trunc(val)
                stack.append(int(val))
        
        return stack.pop()
        '''


        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                right, left = stack.pop(), stack.pop()
                stack.append(left - right)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                right, left = stack.pop(), stack.pop()
                stack.append(int(float(left)/ right))
            else:
                stack.append(int(c))
        return stack.pop()


        
