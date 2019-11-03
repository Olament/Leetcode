#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        def search(node):
            if not node:
                return
            search(node.left)
            lst.append(node.val)
            search(node.right)
        
        search(root)

        return lst
# @lc code=end

