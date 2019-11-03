#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def search(node1, node2):
            if (node1 and not node2) or (not node1 and node2):
                return False

            if not node1 and not node2:
                return True
            
            if node1.val != node2.val:
                return False
            
            left = search(node1.left, node2.left)
            right = search(node1.right, node2.right)

            return left and right
        
        return search(p, q)

        
# @lc code=end

