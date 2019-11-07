#
# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        if n < 2:
            return 0
        cost = [0 for i in range(n)]

        for i in range(1, n):
            for j in range(i//2, -1, -1):
                if (i+1) % (j+1) == 0:
                    if cost[i] == 0:
                        cost[i] = (i+1) // (j+1) + cost[j]
                    else:
                        cost[i] = min(cost[i], (i+1) // (j+1) + cost[j])
        print(cost)
        return cost[-1]
    
        
# @lc code=end

