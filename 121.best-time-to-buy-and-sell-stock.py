#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        lowestPrice = prices[0]
        profit = 0

        for price in prices:
            profit = max(profit, price-lowestPrice)
            lowestPrice = min(lowestPrice, price)
        
        return profit

        
# @lc code=end

