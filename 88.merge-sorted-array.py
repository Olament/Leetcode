#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        for i in range(m+n-1, -1, -1):
            if p1 < 0:
                nums1[i] = nums2[p2]
                p2 -= 1
                continue
            if p2 < 0:
                nums1[i] = nums1[p1]
                p1 -= 1
                continue
                
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1

         


        
# @lc code=end

