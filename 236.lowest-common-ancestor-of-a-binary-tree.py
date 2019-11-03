#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
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
        self.best = (root, 0)
        def search(node, depth):
            if not node:
                return (False, False)
            
            l_p, l_q = search(node.left, depth+1)
            r_p, r_q = search(node.right, depth+1)

            hasp = (node.val == p.val) or l_p or r_p
            hasq = (node.val == q.val) or l_q or r_q

            if hasp and hasq:
                _, bestdepth = self.best
                if depth > bestdepth:
                    self.best = (node, depth)
            
            return hasp, hasq
        
        search(root, 0)
        common, _ = self.best
        return common

# @lc code=end

