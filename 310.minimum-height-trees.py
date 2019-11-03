#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def bfs(node: int) -> int:
            queue = [node]
            visited = [n for _ in range(n)]
            visited[node] = 0
            while len(queue) != 0:
                currNode = queue.pop()
                if visited[currNode] > minDepthVal:
                    return n
                for vertex in adj[currNode]:
                    if visited[vertex] > visited[currNode] + 1:
                        queue.append(vertex)
                        visited[vertex] = visited[currNode] + 1
            return max(visited)

        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        
        minDepthIndex = []
        minDepthVal = n
        for i in range(n):
            depth = bfs(i)
            if depth == minDepthVal:
                minDepthIndex.append(i)
            if depth < minDepthVal:
                minDepthIndex = [i]
                minDepthVal = depth
        
        print(depth)
        
        return minDepthIndex
# @lc code=end

