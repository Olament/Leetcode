#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if len(grid) == 0:
            return 0

        def gridToInt(x: int, y: int) -> int:
            return x * len(grid[0]) + y
        
        def root(i: int) -> int:
            curr = i
            while curr != lst[curr]:
                lst[curr] = lst[lst[curr]]
                curr = lst[curr]
            return curr

        def merge(i: int, j: int):
            if root(i) != root(j):
                lst[root(j)] = root(i)
        
        lst = [i for i in range(0, len(grid) * len(grid[0]))]

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (grid[x][y] == "1"):
                    currIndex = gridToInt(x, y)
                    if x - 1 >= 0 and grid[x-1][y] == "1":
                         merge(currIndex, gridToInt(x - 1, y))
                    if x + 1 < len(grid) and grid[x+1][y] == "1": 
                        merge(currIndex, gridToInt(x + 1, y))
                    if y - 1 >= 0 and grid[x][y-1] == "1": 
                        merge(currIndex, gridToInt(x, y - 1))
                    if y + 1 < len(grid[0]) and grid[x][y+1] == "1": 
                        merge(currIndex, gridToInt(x, y + 1))

        unique = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (grid[x][y] == "1"):
                    currIndex = gridToInt(x, y)
                    print('%d '%(root(currIndex)), end='')
                    if root(currIndex) not in unique:
                        unique.append(root(currIndex))
                else:
                    print('x ', end='')
            print()

        return len(unique)

        
# @lc code=end

