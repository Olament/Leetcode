#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class Solution:
    def compare(self, num1, num2):
        return str(num1) + str(num2) > str(num2) + str(num1) 
    
    def swap(self, arr, i, j):
        if i == j:
            return
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            maxIndex = i
            for j in range(i+1, len(nums)):
                if self.compare(nums[j], nums[maxIndex]):
                    maxIndex = j
            self.swap(nums, i, maxIndex)
        
        maxNumber = ""
        for num in nums:
            maxNumber += str(num)

        return str(int(maxNumber))
        
# @lc code=end

