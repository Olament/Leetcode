#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        single = set()
        for num in nums:
            if num in single:
                single.remove(num)
            else:
                single.add(num)
        
        return list(single)


        
# @lc code=end

