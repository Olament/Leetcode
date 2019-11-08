#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0] * (n+1)
        ways[0] = 1
        ways[1] = 1

        if n < 2:
            return 1

        for i in range(2, n+1):
            ways[i] += ways[i-1]
            ways[i] += ways[i-2]
        
        return ways[n]
# @lc code=end

