# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        
        # fast goes twice as fast as slow
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # when fast reaches end, slow will be at the middle
        return slow