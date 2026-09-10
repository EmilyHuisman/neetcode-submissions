class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left pointer; lowest value
        # right pointer: highest value

        maxprofit = 0
        buy = prices[0]

        for sell in range(1, len(prices)):
            print('sell', prices[sell])
            maxprofit = max(maxprofit, prices[sell]-buy)
            print("maxprofit", maxprofit)
            #print("calc", prices[sell]-prices[buy])
            buy = min(prices[sell], buy)
            print("buy", buy)
        
        return maxprofit























        '''
        min = float("inf")
        max = 0
        l, r = 0, 1
        for i in range(len(prices)):
            print(prices[i])
            if prices[i] > max:
                max = prices[i]
                print("this is new max", max)
            elif prices[i] < min:
                min = prices[i]
                print("this is new min", min)
        return max-min
        '''