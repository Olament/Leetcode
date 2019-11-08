#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        blockSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        rowSet = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue

                if board[i][j] not in rowSet[i]:
                    rowSet[i].add(board[i][j])
                else:
                    return False
                
                if board[i][j] not in colSet[j]:
                    colSet[j].add(board[i][j])
                else:
                    return False
                
                if board[i][j] not in blockSet[i//3 * 3 + j//3]:
                    blockSet[i//3 * 3 + j//3].add(board[i][j])
                else:
                    return False
        return True
# @lc code=end

