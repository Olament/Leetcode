#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def swap(lst, i, j):
            if i == j:
                return
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
        l = 0
        r = 1
        while (r < len(nums)):
            if nums[r] == nums[l]:
                r += 1
            else:
                swap(nums, l+1, r)
                l += 1
                r += 1

        return l+1

# @lc code=end

