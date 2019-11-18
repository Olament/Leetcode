#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    # def numSquares(self, n: int) -> int:
    #     if n <= 1:
    #         return n

    #     dp = [float('inf') for i in range(n+1)]
    #     dp[0] = 0

    #     for i in range(1, len(dp)):
    #         for j in range(1, int(i**0.5)+1):
    #             dp[i] = min(dp[i], dp[i-j*j]+1)
            
    #     return dp[n]
    
    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(1, int(n**0.5)+1):
            squares.append(i**2)
        
        currStep, nextStep, step = {n}, set(), 1
        while currStep:
            for curr in currStep:
                for square in squares:
                    if curr - square < 0:
                        break
                    if curr == square:
                        return step
                    nextStep.add(curr-square)
            currStep, nextStep, step = nextStep, set(), step+1
        
            


# @lc code=end

