#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []

        if not root:
            return lst
        
        queue = []
        queue.append(root)

        while len(queue) > 0:
            currNode = queue.pop()

            lst.append(currNode.val)

            if currNode.right:
                queue.append(currNode.right)
            if currNode.left:
                queue.append(currNode.left)
        
        return lst
            
        
        
# @lc code=end

