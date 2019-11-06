#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}
        prev = None
        curr = head

        while curr:
            if curr not in dic:
                dic[curr] = Node(curr.val, curr.next, curr.random)
            
            if prev:
                prev.next = dic[curr]
            else:
                head = dic[curr]
            
            if curr.random:
                if curr.random not in dic:
                    dic[curr.random] = Node(curr.random.val, curr.random.next, curr.random.random)
                dic[curr].random = dic[curr.random]
            
            prev = dic[curr]
            curr = curr.next
        return head
                
        
# @lc code=end

