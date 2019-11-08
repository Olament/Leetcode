#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        lst = []
        def search(node, depth):
            if not node:
                return

            if len(lst) < depth+1:
                lst.append([])
            if depth % 2 == 0:
                lst[depth].append(node.val)
            else:
                lst[depth].insert(0, node.val)
            
            search(node.left, depth+1)
            search(node.right, depth+1)
        
        search(root, 0)
        return lst

# @lc code=end

