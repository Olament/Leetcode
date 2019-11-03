#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:

        if len(citations) == 0:
            return 0

        citations.sort(reverse=True)
        hindex = 0
        for i in range(len(citations)):
            if citations[i] >= (i+1):
                hindex = (i+1)
            else:
                break
                
        return hindex
# @lc code=end

