#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s:
            return 0

        lb = 0
        currentSum = 0
        minLength = len(nums)
        for i in range(len(nums)):
            currentSum += nums[i]
            while currentSum >= s:
                minLength = min(minLength, i-lb+1)
                currentSum -= nums[lb]
                lb += 1
        return minLength
        
# @lc code=end

