#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        
        cost = [triangle[0][0]]
        
        for i in range(1, len(triangle)):
            newCost = []
            for j in range(i+1):
                val1 = cost[j-1]+triangle[i][j] if j > 0 else float('inf')
                val2 = cost[j]+triangle[i][j] if j < i else float('inf')
                newCost.append(min(val1, val2))
            print(newCost)
            cost = newCost
        return min(cost)
# @lc code=end

