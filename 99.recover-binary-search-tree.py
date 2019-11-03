#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def swap(rnode, lnode):
            temp = rnode.val
            rnode.val = lnode.val
            lnode.val = temp
        
        def search(node, minb, maxb):
            if not node:
                return
            
            search(node.left, minb, node.val - 1)
            search(node.right, node.val + 1, maxb)

            if node.right and not(node.val < node.right.val and node.right <= maxb):
                swap(node.right, node)
                return
            
            if node.left and not(minb <= node.left.val and node.left.val < node.val):
                swap(node.left, node)
                return


        search(root, -float('inf'), float('inf'))
            
        
# @lc code=end

