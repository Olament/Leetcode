#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        slow, fast = 0, 0
        res = 0
        while slow < len(height):
            fast = slow + 1

            print(slow)
            print(fast)
            print()
            # left pointer cannot start with zero
            if height[slow] == 0:
                slow += 1
                continue
                
            # search for right pointer
            while fast < len(height) and height[fast] == 0:
                fast += 1
            
            # if we didnot find any avaliable fast, try next one
            if fast >= len(height):
                slow += 1
            else:
                minHeight = min(height[fast], height[slow])
                for i in range(slow+1, fast):
                    res += minHeight - height[i]
                slow = fast
        
        return res
# @lc code=end

