''' A key (integer), value (string) pair is given at a time. It only prints value in sequence of ascending order of keys. If the key is not in order, it doesn’t print its string value and only prints the value until it sees the next key in order.

When it goes through all the keys, it prints the remaining values in order if no value in the sequence is missing. Only one pair of key and value is given at a time. There is no list.  '''
class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.pos = 0
        self.vals = [None] * n 
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        idKey -= 1  # making it 0-based
        self.vals[idKey] = value
        if idKey > self.pos: return []
        else:
            while self.pos < len(self.vals) and self.vals[self.pos]:
                self.pos += 1
            return self.vals[idKey:self.pos]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)