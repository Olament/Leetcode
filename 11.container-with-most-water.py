#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp = 0
        rp = len(height) - 1
        vol = (len(height) - 1) * min(height[lp], height[rp])
        for i in range(0, len(height) - 1, 1):
            if height[lp] < height[rp]:
                lp += 1
                newVol = (rp-lp) * min(height[lp], height[rp])
            else:
                rp -= 1
            newVol = (rp-lp) * min(height[lp], height[rp])
            if newVol > vol:
                vol = newVol
        return vol
            


# @lc code=end

