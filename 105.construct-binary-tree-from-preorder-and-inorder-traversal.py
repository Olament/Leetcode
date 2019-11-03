#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def search(preorder, inorder) -> TreeNode:
            if not inorder:
                return None
            index = inorder.index(preorder.pop(0))
            node = TreeNode(inorder[index])
            node.left = search(preorder, inorder[0:index])
            node.right = search(preorder, inorder[index+1:])

            return node
        
        root = search(preorder, inorder)
        return root

        



# @lc code=end

