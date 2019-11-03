#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n:
            return 1
            
        dp = [0]*(n)
        dp[0] = 9
        for i in range(1,n):
            dp[i] = dp[i-1]*(10-i)
        return sum(dp)+1
# @lc code=end

