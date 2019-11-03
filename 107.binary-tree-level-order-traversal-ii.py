#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        lst = []
        queue = []

        queue.append(root)
        while len(queue) > 0:
            newQueue = []
            for i in range(len(queue)):
                currNode = queue[i]
                if currNode.left:
                    newQueue.append(currNode.left)
                if currNode.right:
                    newQueue.append(currNode.right)
                queue[i] = currNode.val
            
            lst.insert(0, queue)
            queue = newQueue
        
        return lst
    
# @lc code=end

