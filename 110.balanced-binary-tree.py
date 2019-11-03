#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def search(node):
            if not node:
                return (0, True)
            
            l_depth, l_valid = search(node.left)
            r_depth, r_valid = search(node.right)

            curr_depth = max(l_depth, r_depth) + 1
            curr_valid = (abs(l_depth-r_depth) <= 1) and l_valid and r_valid
        
            return curr_depth, curr_valid

        _, valid = search(root)
        return valid

        
        
# @lc code=end

