#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cache = [0] * len(nums)
        for i in range(len(nums)):
            cache[(i+k)%len(nums)] = nums[i]

        for i in range(len(nums)):
            nums[i] = cache[i]
        
        
# @lc code=end

