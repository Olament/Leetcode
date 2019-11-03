#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def dfs(node, depth, lst):
            if not node:
                return
            if len(lst) < depth+1:
                lst.append(node)
            else:
                node.next = lst[depth]
                lst[depth] = node
            
            dfs(node.right, depth+1, lst)
            dfs(node.left, depth+1, lst)
        
        dfs(root, 0, [])
        return root

        
# @lc code=end

