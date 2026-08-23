class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            left_h = heights[l]
            right_h = heights[r]
            volume = (r - l) * min(left_h, right_h)
            maximum = max(volume, maximum)
            if left_h < right_h:
                l += 1
            else:
                r -= 1
        
        return maximum