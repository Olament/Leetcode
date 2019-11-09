#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def search(lb, rb, arr, tar):
            while lb <= rb:
                mid = lb + (rb-lb) // 2
                if arr[mid] == tar:
                    return mid
                elif arr[mid] > tar:
                    rb = mid - 1
                else:
                    lb = mid + 1
            return -1
        
        for i in range(len(numbers)):
            index = search(i+1, len(numbers)-1, numbers, target-numbers[i])
            if index != -1:
                return [i+1, index+1]
        return [0, 0]

        
# @lc code=end

