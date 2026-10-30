class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''

        for each day finding the first day (if it exists) that has a higher temp
        in an array return how many days in the future, otherwise 0


        traverse thru temp list in reverse

        add values to a stack ()

        popping value is 1 day

        
        * stack in descending order (store indexs not values)
        1. traverse list in reverse
            
            - whil stack adn temp > stack.peak (* check index in list)
                - pop value
            - if empty return 0
            subtract indices for day value and add to ans array (@ index of temp)
            add index to stack

        '''
        stack = []
        ans = [0] * len(temperatures)
        for idx in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[idx] >= temperatures[stack[-1]]:
                stack.pop()
            
            if not stack:
                stack.append(idx)
                continue
            
            ans[idx] = stack[-1] - idx
            stack.append(idx)
        
        
        return ans
            



















