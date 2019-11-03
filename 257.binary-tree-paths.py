#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        lst = []

        if root == None:
            return lst

        def search(node: TreeNode, path: str):
            if node.right == None and node.left == None:
                lst.append(path+str(node.val))
                return
    
            if node.right != None:
                search(node.right, path+str(node.val)+"->")
            if node.left != None:
                search(node.left, path+str(node.val)+"->")
        
        search(root, "")
        return lst
            
                 
# @lc code=end

