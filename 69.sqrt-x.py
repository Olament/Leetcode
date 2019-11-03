#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        lb = 0
        rb = x

        if x == 1:
            return 1
        if x == 0:
            return 0

        while (lb+1 < rb):
            mid = lb + (rb - lb) // 2
            sqrt = mid * mid

            if sqrt == x:
                return mid
            elif sqrt < x:
                lb = mid
            else:
                rb = mid-1
        
        if rb * rb <= x:
            return rb
        return lb


        
# @lc code=end

