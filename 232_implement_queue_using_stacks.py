class MyQueue(object):

    def __init__(self):
        self.queue = []
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        # empty queue into stack
        for i in range(len(self.queue)):
            self.stack.append(self.queue.pop())
            
        top = self.stack.pop()  # top of stack is first item in queue
        
        # empty stack back into queue
        for i in range(len(self.stack)):
            self.queue.append(self.stack.pop())
            
        return top
        

    def peek(self):
        """
        :rtype: int
        """
        return self.queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()