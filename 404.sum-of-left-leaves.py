#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def search(node, isleftnode):
            if not node:
                return 0
            
            if not node.right and not node.left and isleftnode:
                return node.val
            
            return search(node.left, True)+search(node.right, False)
        
        return search(root, False)

            
        
# @lc code=end

