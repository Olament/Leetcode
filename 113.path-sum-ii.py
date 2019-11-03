#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        lst = []
        def search(node, csum, path):
            if not node:
                return
            
            csum = csum + node.val
            newpath = path + [node.val]
            
            if not node.right and not node.left and csum == sum:
                lst.append(newpath)
            
            search(node.right, csum, newpath)
            search(node.left, csum, newpath)
        
        search(root, 0, [])

        return lst
            
# @lc code=end

