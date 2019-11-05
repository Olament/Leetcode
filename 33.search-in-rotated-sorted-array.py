#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## determine the rotate point
        lb, rb = 0, len(nums)-1
        while (lb <= rb):
            mid = lb + (rb-lb) // 2
            if nums[mid] == target:
                return mid
            elif nums[lb] <= nums[mid]:
                if nums[lb] <= target <= nums[mid]:
                    rb = mid - 1
                else:
                    lb = mid + 1
            else:
                if nums[mid] <= target <= nums[rb]:
                    lb = mid + 1
                else:
                    rb = mid - 1
        return -1

        
# @lc code=end

