#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0:
            return True
        if len(board) == 0 or len(board[0]) == 0:
            return False
        
        def search(x, y, grid, word):
            if len(word) == 0:
                return True
            
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or word[0] != grid[x][y]:
                return False
            
            temp = grid[x][y]
            grid[x][y] = "#"
            result = search(x+1, y, grid, word[1:]) or search(x, y+1, grid, word[1:]) or \
                search(x-1, y, grid, word[1:]) or search(x, y-1, grid, word[1:])
            grid[x][y] = temp

            return result
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(i, j, board, word):
                    return True
            
        

        
# @lc code=end

