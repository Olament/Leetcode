#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        lst = []
        def search(node, depth):
            if not node:
                return
            
            if len(lst) < depth+1:
                lst.append(node.val)
            else:
                lst[depth] = node.val
            
            search(node.left, depth+1)
            search(node.right, depth+1)
        
        search(root, 0)
        return lst
# @lc code=end

