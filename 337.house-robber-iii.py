#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        self.sum = 0

        def search(node):
            if not node:
                return 0, 0
            
            leftcurr, left = search(node.left)
            rightcurr, right = search(node.right)

            return node.val+left+right, max(left, leftcurr)+max(right, rightcurr)

        sum1, sum2 = search(root)
        return max(sum1, sum2)        
        
# @lc code=end

