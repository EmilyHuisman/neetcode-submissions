class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left pointer; lowest value
        # right pointer: highest value

        maxprofit = 0
        buy = prices[0]

        for sell in prices:
            maxprofit = max(maxprofit, sell-buy)
            buy = min(sell, buy)
        
        return maxprofit