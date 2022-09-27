class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.prev = [homepage]  # history stack
        self.next = []  # forward stack
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.prev.append(url)
        self.next = []  # reset forward stack
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps and len(self.prev) > 1:
            # always keep at least one element in prev
            self.next.append(self.prev.pop())
            steps -= 1
        return self.prev[-1]
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps and self.next:
            # next can have 0 elements
            self.prev.append(self.next.pop())
            steps -= 1
        return self.prev[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)