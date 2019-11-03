#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minIndex = 0
        
    def push(self, x: int) -> None:
        if len(self.stack) != 0 and x < self.stack[self.minIndex]:
            self.minIndex = len(self.stack)
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack = self.stack[0:len(self.stack) - 1]
        else:
            return
        
        self.minIndex = self.update()
    
    def update(self) -> int:
        if len(self.stack) == 0:
            return 0

        minValue = self.stack[0]
        index = 0
        for i in range(1, len(self.stack)):
            if self.stack[i] < minValue:
                minValue = self.stack[i]
                index = i
        
        return index

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.stack[self.minIndex]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

