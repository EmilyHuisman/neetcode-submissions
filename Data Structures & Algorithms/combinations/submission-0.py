class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(i, curSet, combination, n, k):
            if len(curSet) == k:
                combination.append(curSet.copy())
                return
            if i > n:
                return
            

            curSet.append(i)
            helper(i+1, curSet, combination, n, k)

            curSet.pop()
            helper(i+1, curSet, combination, n, k)


        curSet, combination = [], []
        helper(1, curSet, combination, n, k)
        return combination