#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            for closeNumber in range(nums[i]-t, nums[i]+t+1):
                if closeNumber in dic and i - dic[closeNumber] <= k:
                    return True
            dic[nums[i]] = i
        return False
# @lc code=end

