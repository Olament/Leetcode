#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def dfs(self, curr, visited, edgeList):
        if visited[curr] == -1:
            return False
        if visited[curr] == 1:
            return True
        
        visited[curr] = -1
        for node in edgeList[curr]:
            if not self.dfs(node, visited, edgeList):
                return False
        
        visited[curr] = 1
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edgeList = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            edgeList[edge[0]].append(edge[1])
        
        visited = [0] * numCourses
        for i in range(numCourses):
            if not self.dfs(i, visited, edgeList):
                return False
        return True
        
        
        
# @lc code=end

