#
# @lc app=leetcode id=419 lang=python3
#
# [419] Battleships in a Board
#

# @lc code=start
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0
        
        def search(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            if board[i][j] == '.':
                return

            board[i][j] = '.'
            search(i+1, j)
            search(i, j+1)
            search(i-1, j)
            search(i, j-1)

        numberOfShip = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    numberOfShip += 1
                    search(i, j)

        return numberOfShip     
# @lc code=end

