#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def search(node):
            if not node:
                return 0
            
            if not node.left or not node.right:
                return max(search(node.left), search(node.right)) + 1
            return min(search(node.left), search(node.right)) + 1
        
        return search(root)
            

        
# @lc code=end

