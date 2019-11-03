#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        globsum = nums[0]
        localsum = nums[0]

        for i in nums[1:]:
            localsum = max(i, localsum+i)
            globsum = max(globsum, localsum)
        
        return globsum

# @lc code=end

