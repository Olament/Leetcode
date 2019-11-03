#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        def search(node):
            if not node:
                return
            
            search(node.left)
            search(node.right)

            lst.append(node.val)
        
        search(root)
        return lst
# @lc code=end

