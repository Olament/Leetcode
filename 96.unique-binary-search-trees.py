#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        if n < 2:
            return n

        lst = [0 for i in range(n+1)]
        lst[0] = 1
        lst[1] = 1
        for i in range(2, n+1):
            lst[i] = 0
            for j in range(1, i+1):
                left = j-1
                right = i-j

                lst[i] += lst[left] * lst[right]

        return lst[n]
        
# @lc code=end

