#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        def search(node, tempsum):   
            if not node:
                return False 

            newsum = tempsum + node.val
            if newsum == sum:
                if not node.right and not node.left:
                    return True
            
            return search(node.left, newsum) or search(node.right, newsum)
        
        return search(root, 0)

                
            
# @lc code=end

