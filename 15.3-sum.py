#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        lst = []
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                needNum = -(nums[i] + nums[j])
                if needNum in dic:
                    for num in dic[needNum]:
                        lst.append([nums[i], nums[j], nums[num]])

        return lst
# @lc code=end

