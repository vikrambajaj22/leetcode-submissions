# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
            # both l1 and l2 are non-empty
            result = sorted_list = ListNode()
            while l1 and l2:
                if l1.val > l2.val:
                    sorted_list.next = l2
                    l2 = l2.next
                else:
                    sorted_list.next = l1
                    l1 = l1.next
                sorted_list = sorted_list.next
            # capture remaining elements (if any) in l1 or l2
            sorted_list.next = l1 or l2
            return result.next  # points to start of sorted_list
        else:
            # either l1 or l2 is empty (or both are)
            # return whichever is non-empty, or None
            return l1 or l2
