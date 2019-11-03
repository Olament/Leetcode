#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def search(curr: TreeNode):
            if curr == None:
                return
            
            if len(lst) == k:
                return
            
            search(curr.left)
            lst.append(curr.val)
            search(curr.right)
        
        lst = []
        search(root)

        return lst[k-1]
# @lc code=end

