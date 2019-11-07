#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        lst = []
        def bfs(node, depth):
            if not node:
                return
            
            if len(lst) <= depth:
                lst.append(0)
            
            lst[depth] = node.val
            bfs(node.right, depth+1)
            bfs(node.left, depth+1)

        bfs(root, 0)

        return lst[-1]
# @lc code=end

