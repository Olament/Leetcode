#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def search(node):
            if not node:
                return
            
            temp = node.right
            node.right = node.left
            node.left = temp

            search(node.left)
            search(node.right)
        
        search(root)
        return root
# @lc code=end

