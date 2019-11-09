#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def search(i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == 'A' or board[i][j] == 'X':
                return
            
            board[i][j] = 'A'
            search(i+1, j)
            search(i-1, j)
            search(i, j+1)
            search(i, j-1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i in [0, len(board)-1] or j in [0, len(board[0])-1] and board[i][j] == 'O':
                    search(i, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'
# @lc code=end

