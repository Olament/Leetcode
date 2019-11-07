#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        res = [1 for i in range(len(nums))]
        maxL = 0
        for i in range(1, len(nums)):
            for j in range(i, -1, -1):
                if nums[i] > nums[j]:
                    res[i] = max(res[i], res[j]+1)
            maxL = max(res[i], maxL)
        return maxL

                

# @lc code=end

