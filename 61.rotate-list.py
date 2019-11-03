#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        length = 0
        p = dummy
        while p and p.next:
            length += 1
            p = p.next

        if length == 0:
            return head
        
        newk = k % length

        for _ in range(newk):
            fast = fast.next
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None

        return dummy.next
# @lc code=end

