#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = {}
        for fr, to in tickets:
            if fr not in edges:
                edges[fr] = set()
            edges[fr].add(to)
        
        stack = ['JFK']
        route = []

        while stack:
            curr = stack[-1]
            while edges[curr]:
                stack.append(edges[curr].pop())
            route.append(stack.pop())
        return route
                   
# @lc code=end

