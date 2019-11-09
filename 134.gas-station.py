#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        pos, gasLevel = 0, 0
        for i in range(len(gas)):
            if gas[i] + gasLevel >= cost[i]:
                gasLevel += gas[i]-cost[i]
            else:
                pos, gasLevel = i+1, 0
            
        return pos
# @lc code=end

