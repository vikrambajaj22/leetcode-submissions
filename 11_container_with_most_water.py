class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        left, right = 0, len(height)-1
        
        # start with water between extreme left and right
        # now keep narrowing in
        # since the width is decreasing, the only way the area can be maximized is if the height was increasing, so only keep a height under consideration if it is longer, otherwise move from it (left or right)
        while left < right:
            water = max(water, (right-left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
        return water