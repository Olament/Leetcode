#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        queue = []
        queue.append((root.left, root.right))
        
        while len(queue) > 0:
            left, right = queue[0]
            queue = queue[1:]

            if not left and not right:
                continue
                
            if not left or not right:
                return False

            if left.val != right.val:
                return False
            
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        
        return True

# @lc code=end

