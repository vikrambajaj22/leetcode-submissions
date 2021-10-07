class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # every element of stack contains (pushed_value, current_minimum)
        if not self.stack:
            # better not to use a self.min variable since stack can become emtpty after
            # multiple pops and then min would have to be reset
            self.stack.append((val, val))
        else:
            # (pushed_value, min(prev_minimum, pushed_value))
            self.stack.append((val, min(self.stack[-1][1], val)))
        # print('after push: ', self.stack)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        # print('after pop: ', self.stack)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
