#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def search(node, minb, maxb):
            if not node:
                return True

            # right = str(node.right.val) if node.right else 'null'
            # left = str(node.left.val) if node.left else 'null'
            # print(str(node.val) + " " + left + " " + right)

            if node.right and not(node.val < node.right.val and node.right.val <= maxb):
                return False
            if node.left and not(minb <= node.left.val and node.left.val < node.val):
                return False
            
            left = search(node.left, minb, node.val-1)
            right = search(node.right, node.val + 1, maxb)

            return left and right
        
        return search(root, -float('inf'), float('inf'))
# @lc code=end

