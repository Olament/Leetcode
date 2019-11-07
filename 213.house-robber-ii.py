#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def simple_rob(nums):
            not_rob, rob = 0, 0
            for num in nums:
                rob, not_rob = not_rob+num, max(rob, not_rob)
            return max(rob, not_rob)
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))
        
        
# @lc code=end

