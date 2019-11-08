#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        indexMax = 0
        for i in range(len(nums)):
            if nums[i] > nums[indexMax]:
                indexMax = i
        
        node = TreeNode(nums[indexMax])
        node.left = self.constructMaximumBinaryTree(nums[:indexMax])
        node.right = self.constructMaximumBinaryTree(nums[indexMax+1:])

        return node
# @lc code=end

