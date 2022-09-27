class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        
        total = 0
        
        while left < right:
            left_height = height[left]
            right_height = height[right]
            
            if left_height < right_height:
                if left_height >= left_max:
                    left_max = left_height
                else:
                    total += left_max - left_height
                left += 1
            else:
                if right_height >= right_max:
                    right_max = right_height
                else:
                    total += right_max - right_height
                right -= 1
                
        return total