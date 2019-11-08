#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        cost = [0 for i in range(len(prices))]
        for i in range(1, len(prices)):
            cost[i] = max(cost[i-1], cost[i-1]+(prices[i] - prices[i-1]))
        
        return cost[-1]
        
# @lc code=end

