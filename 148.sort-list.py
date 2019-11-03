#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:        
    def sortList(self, head: ListNode) -> ListNode:
        def split(root):
            slow = root
            fast = root.next

            while fast and fast.next and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            second = slow.next
            slow.next = None
            
            # print(root)
            # print(second)
            return root, second 
        
        def mergelist(lst1, lst2):
            p1 = lst1
            p2 = lst2
            lst = ListNode(0)
            p = lst

            while p1 and p2:
                if p1.val < p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
                p = p.next
            
            p.next = p1 if p1 else p2
            return lst.next
        
        def merge(lst):
            if not lst:
                return None
            
            if not lst.next:
                return lst
            
            first, second = split(lst)
            l = merge(first)
            r = merge(second)

            return mergelist(l, r)

        
        return merge(head)
        

        
# @lc code=end

