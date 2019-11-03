#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []

        def search(lb: int, rb: int):
            if lb > rb:
                return [None]
            trees = []
            for i in range(lb, rb+1):
                for left in search(lb, i-1):
                    for right in search(i+1, rb):
                        node = TreeNode(i)
                        node.left = left
                        node.right = right
                        trees.append(node)
            return trees
        
        tree = search(1, n)
        return tree
            
            
# @lc code=end

