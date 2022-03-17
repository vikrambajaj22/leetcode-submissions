# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        curr = head

        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next  # skipping over curr.next
            else:
                curr = curr.next

        return head
