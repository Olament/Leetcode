#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        copyNode = Node(node.val, [])
        visited[node] = copyNode
        stack = [node]

        while len(stack) > 0:
            currNode = stack.pop()
            for neighbor in currNode.neighbors:
                if neighbor in visited:
                    visited[currNode].neighbors.append(visited[neighbor])
                else:
                    newNode = Node(neighbor.val, [])
                    visited[neighbor] = newNode
                    visited[currNode].neighbors.append(newNode)
                    stack.append(newNode)
        
        return copyNode



# @lc code=end

