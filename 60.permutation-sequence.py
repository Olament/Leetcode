#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        lst = [i for i in range(1, n+1)]
        k -= 1
        per = ''

        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            per += str(lst[index])
            lst.remove(lst[index])
        
        return per
        
# @lc code=end

