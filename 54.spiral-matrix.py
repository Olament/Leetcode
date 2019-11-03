#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def left(x: int, y: int) -> (int, int):
            return (x, y + 1)
        def right(x: int, y: int) -> (int, int):
            return (x, y - 1)
        def up(x: int, y: int) -> (int, int):
            return (x - 1, y)
        def down(x: int, y: int) -> (int, int):
            return (x + 1, y)

        lst = []
        funcLst = [left, down, right, up]
        xstep = len(matrix)
        ystep = len(matrix[0])
        pos = 0
        x = 0
        y = 0
        while len(lst) < len(matrix) * len(matrix[0]):
            move = funcLst[pos]
            if move == left or move == right:
                for i in range(ystep):
                    lst.append(matrix[x][y])
                    x, y = move(x, y)
            else:
                for i in range(xstep):
                    lst.append(matrix[x][y])
                    x, y = move(x, y)
            pos = (pos + 1) % 4
        
        return lst


# @lc code=end

