#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def search(nums, lb, rb) -> TreeNode:
            if lb > rb:
                return None
            mid = lb + (rb - lb) // 2
            node = TreeNode(nums[mid])
            node.left = search(nums, lb, mid-1)
            node.right = search(nums, mid+1, rb)

            return node
        
        return search(nums, 0, len(nums)-1)
        
            

        
# @lc code=end

