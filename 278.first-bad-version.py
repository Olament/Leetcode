#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lb, rb = 1, n
        while lb < rb:
            mid = lb + (rb-lb) // 2
            isBad = isBadVersion(mid)
            if isBad:
                rb = mid
            else:
                lb = mid + 1
        
        return lb

        
# @lc code=end

