# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        slow = head

        # let fast move n steps forward
        for _ in range(n):
            fast = fast.next

        if not fast:
            # if fast is None, it means n==len(list)
            # so, to remove nth from end, we must remove first node
            return head.next

        # now, move slow and fast together
        # slow will move len(list)-n steps
        while fast.next:
            fast = fast.next
            slow = slow.next

        # now, fast.next is None and slow.next points to nth node from end
        slow.next = slow.next.next

        return head
