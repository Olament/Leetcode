#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            dfs(node.left)

            node.right = self.prev
            node.left = None
            self.prev = node
        
        dfs(root)
        
# @lc code=end

