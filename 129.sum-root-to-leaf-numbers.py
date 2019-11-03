#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.tsum = 0
        def search(node, temp):
            if not node:
                return 
            
            newtemp = temp*10 + node.val

            if not node.right and not node.left:
                self.tsum += newtemp
                return
            
            search(node.left, newtemp)
            search(node.right, newtemp)
        
        search(root, 0)
        return self.tsum

# @lc code=end

