#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftsearch(lst, t):
            lb, rb = 0, len(lst) - 1
            while (lb <= rb):
                mid = (lb+rb) // 2
                if target > lst[mid]:
                    lb = mid + 1
                else:
                    rb = mid - 1
            return lb
        def rightsearch(lst, t):
            lb, rb = 0, len(lst) - 1
            while (lb <= rb):
                mid = lb + (rb - lb) // 2
                if (lst[mid] == t) and (mid == len(nums)-1 or lst[mid] < lst[mid+1]):
                    return mid
                elif lst[mid] > t:
                    rb = mid - 1
                else:
                    lb = mid + 1
            return -1
        
        left, right = leftsearch(nums, target), rightsearch(nums, target)
        return (left, right) if left <= right else [-1, -1]

        

# @lc code=end

