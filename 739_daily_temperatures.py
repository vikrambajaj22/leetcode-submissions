class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # brute force is to just look at all next elements for each element O(n^2)
        # use a monotonic stack instead O(N), always storing the index of the higher temperature onto the stack while popping indexes of those lower than it
        # tip: monotonic stack is the standard solution for "next greater element" type problems 
        ans = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                curr = stack.pop()
                ans[curr] = i - curr
            
            stack.append(i)
        
        return ans