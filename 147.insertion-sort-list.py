#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)

        curr = head
        prev = dummy
        nextp = None

        while curr:
            nextp = curr.next

            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            curr.next = prev.next
            prev.next = curr
            prev = dummy
            curr = nextp
        
        return dummy.next




# @lc code=end

