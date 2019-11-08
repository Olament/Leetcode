#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if slow < 2 or nums[fast] != nums[slow-1] or nums[fast] != nums[slow-2]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
# @lc code=end

