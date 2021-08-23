# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, curr):
        prev = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
    
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # find the middle
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next  # goes twice as fast as slow
            slow = slow.next
            
        # slow points to the middle if fast reached the end
        
        # reverse the second half
        slow = self.reverse(slow)
        fast = head  # reset fast to beginning
        
        # compare elements in both halves
        while slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
            
        return True