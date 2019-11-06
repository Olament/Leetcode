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
        if not nums1:
            nums1 = nums2
            return

        index = 0
        while nums2 and index < len(nums1):
            if nums2[0] < nums1[index]:
                for i in range(index, len(nums1), -1):
                    nums1[i+1] = nums1[i]
                nums2 = nums2[1:]
            index += 1
        
        # for i in range(index+1, index+1+len(nums2)):
        #     nums1[i] = nums2[0]
        #     nums2 = nums2[1:]
        


        
# @lc code=end

