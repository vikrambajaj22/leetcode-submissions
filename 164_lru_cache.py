class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.queue = []
        self.cache = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            # update position in queue
            self.queue.remove(key) 
            self.queue.append(key)
            return self.cache[key]
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache[key] = value
            # update position in queue
            self.queue.remove(key) 
            self.queue.append(key)
        else:
            if len(self.cache) == self.capacity:
                evicted_key = self.queue.pop(0)
                del self.cache[evicted_key]
            self.cache[key] = value
            self.queue.append(key)
                
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)