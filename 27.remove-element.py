#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        def swap(lst, i, j):
            if i == j:
                return
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
        
        r = len(nums) - 1
        l = 0
        
        while(l <= r):
            if nums[l] == val:
                swap(nums, l, r)
                r -= 1
            else:
                l += 1
        return l
        
# @lc code=end

