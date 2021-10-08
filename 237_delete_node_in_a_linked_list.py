# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # cannot simply do node = node.next because prev node in the list still points to the old reference 'node'
        # instead, copy over value of the next node into current 'node' and skip over the next node
        node.val = node.next.val  # since node isn't the tail (last node)
        node.next = node.next.next
