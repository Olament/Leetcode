#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def search(node, depth):
            if not node:
                return depth-1
            
            ld = search(node.left, depth+1)
            rd = search(node.right, depth+1)

            return max(ld, rd)
        
        return search(root, 1)
            
# @lc code=end

