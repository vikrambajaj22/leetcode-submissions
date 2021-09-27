class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for op in operations:
            if op in ['--X', 'X--']:
                x -= 1
            elif op in ['++X', 'X++']:
                x += 1

        return x
