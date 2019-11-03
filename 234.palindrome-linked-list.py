#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def split(lst):
            slow = lst
            fast = lst.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            second = slow.next
            slow.next = None
            
            return lst, second
        
        def reverse(lst):
            prev = None
            curr = lst
            nextp = None

            while curr:
                nextp = curr.next
                curr.next = prev
                prev = curr
                curr = nextp
            
            return prev
                
        
        if not head:
            return True
        
        if not head.next:
            return True
        
        first, second = split(head)
        second = reverse(second)

        while first and second:
            if first.val != second.val:
                return False
            
            first = first.next
            second = second.next
    
        return True
        

# @lc code=end

