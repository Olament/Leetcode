#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def split(root):
            slow = root
            fast = root.next

            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            
            second = slow.next
            slow.next = None

            return root, second
        
        def reverse(root):
            prev = None
            curr = root
            nextp = None

            while curr:
                nextp = curr.next
                curr.next = prev
                prev = curr
                curr = nextp
            
            return prev
        
        def merge(lst1, lst2):
            p1 = lst1
            p2 = lst2
            dummy = ListNode(0)
            curr = dummy

            switch = True

            while p1 and p2:
                if switch:
                    curr.next = p1
                    p1 = p1.next
                else:
                    curr.next = p2
                    p2 = p2.next
                switch = not switch
                curr = curr.next
            
            curr.next = p1 if p1 else p2

            return dummy.next

        if not head:
            return head

        first, second = split(head)
        second = reverse(second)
        return merge(first, second)   
# @lc code=end

