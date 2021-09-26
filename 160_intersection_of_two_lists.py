# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = headA
        b = headB

        # logic: traverse to the end of A and B, if either of them reaches the end first, there is a difference of length
        # by reassigning the pointer to the head of the other list, this difference in lengths is accounted for
        # so, the pointers will either meet in the next traversal or both reach end at the same time (if there is no intersection)

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
