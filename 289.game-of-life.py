#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return

        adjMatrix = [[0 for j in range(len(board[0]))] for i in range(len(board))]

        def isValid(x, y):
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                return False
            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                # iterate adj 
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if (x == 0 and y == 0) or not isValid(i+x, j+y):
                            continue
                        if board[i+x][j+y] == 1:
                            adjMatrix[i][j] += 1
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    if adjMatrix[i][j] < 2 or adjMatrix[i][j] > 3:
                        board[i][j] = 0
                else:
                    if adjMatrix[i][j] == 3:
                        board[i][j] = 1       
# @lc code=end

