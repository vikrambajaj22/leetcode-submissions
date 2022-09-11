"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        stack = []
        curr = head
        
        while curr:
            if curr.child:
                if curr.next: stack.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            if stack and not curr.next:
                temp = stack.pop()
                curr.next = temp
                temp.prev = curr
            curr = curr.next
            
        return head