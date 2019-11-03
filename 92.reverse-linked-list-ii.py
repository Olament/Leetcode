#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        for _ in range(m-1):
            pre = pre.next
        
        reverse = None 
        curr = pre.next

        for _ in range(n-m+1):
            nextp = curr.next
            curr.next = reverse
            reverse = curr
            curr = nextp
        pre.next.next = curr
        pre.next = reverse

        return dummy.next
        
# @lc code=end

