#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i*i)
            i += 1
        
        cost = [0]
        for i in range(1, (n+1)):
            minCost = cost[i-1] + 1
            for square in squares:
                if i - square >= 0:
                    minCost = min(minCost, cost[i-square] + 1)
            cost.append(minCost)

        return cost[-1]
                            
# @lc code=end

