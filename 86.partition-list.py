#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = ListNode(0)
        big = ListNode(0)

        smallp = small
        bigp = big

        while head:
            if head.val < x:
                smallp.next = head
                smallp = smallp.next
            else:
                bigp.next = head
                bigp = bigp.next
            head = head.next
        
        smallp.next = big.next
        bigp.next = None
        return small.next

        
# @lc code=end

