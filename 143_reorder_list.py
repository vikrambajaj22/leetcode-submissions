# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, head):
        curr, prev = head, None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # find the middle, reverse the second half
        # then, merge the two halves in an alternating fashion

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        slow = self.reverse(slow)

        res = merged = ListNode()
        l1 = head
        l2 = slow

        while l1 and l2:
            merged.next = l1
            l1 = l1.next
            merged = merged.next

            merged.next = l2
            l2 = l2.next
            merged = merged.next

        merged.next = None  # to prevent the last node from cyclic-ly pointing to itself

        return res.next
