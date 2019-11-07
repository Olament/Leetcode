#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return nums

        heap = Heap()
        for num in nums:
            heap.insert(num)
        
        kth = 0
        for _ in range(k):
            kth = heap.delete()
        
        return kth

class Heap:
    def __init__(self):
        self.arr = [0]
        self.size = 0
    
    def insert(self, num):
        self.arr.append(num)
        self.size += 1
        self.swim(self.size)
    
    def peak(self):
        if self.size > 0:
            return self.arr[1]
        return None
    
    def delete(self):
        if self.size == 0:
            return None
        
        toReturn = self.arr[1]
        self.__swap(1, self.size)
        self.arr.pop()
        self.size -= 1
        self.sink(1)

        return toReturn
    
    def swim(self, index):
        while index > 1 and (self.arr[index//2] < self.arr[index]):
            self.__swap(index, index//2)
            index = index // 2

    def sink(self, index):
        while index*2 <= self.size:
            nextIndex = self.__nextIndex(index)
            if self.arr[index] < self.arr[nextIndex]:
                self.__swap(index, nextIndex)
            index = nextIndex

    def __nextIndex(self, index):
        if 2 * index + 1 > self.size:
            return 2*index
        elif self.arr[2*index] > self.arr[2*index+1]:
            return 2*index
        else:
            return 2*index+1
            
    def __swap(self, i, j):
        if i == j:
            return
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp      
# @lc code=end

