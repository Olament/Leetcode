#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(node):
            if not node:
                return None
            
            if max(p.val, q.val) < node.val:
                return search(node.left)
            elif min(p.val, q.val) > node.val:
                return search(node.right)
            else:
                return node
        return search(root)
            
            
# @lc code=end

