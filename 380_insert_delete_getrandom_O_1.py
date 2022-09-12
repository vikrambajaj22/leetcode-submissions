class RandomizedSet(object):

    def __init__(self):
        self.vals = set()
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.vals:
            self.vals.add(val)
            return True
        return False
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.vals:
            self.vals.remove(val)
            return True
        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        index = random.randint(0, len(self.vals)-1)
        return list(self.vals)[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()