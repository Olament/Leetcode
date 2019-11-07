#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])

        if len(points) < 2:
            return len(points)

        currInterval = points[0]
        numberOfShot = 1

        for i in range(1, len(points)):
            if currInterval[1] < points[i][0]:
                numberOfShot += 1
                currInterval = points[i]
            else:
                currInterval = [points[i][0], min(points[i][1], currInterval[1])]
        
        return numberOfShot


# @lc code=end

