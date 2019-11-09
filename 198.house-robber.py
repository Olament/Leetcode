#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob, not_rob = 0, 0
        for num in nums:
            rob, not_rob = (num)+not_rob, max(rob, not_rob)
        return max(rob, not_rob)
        
# @lc code=end

