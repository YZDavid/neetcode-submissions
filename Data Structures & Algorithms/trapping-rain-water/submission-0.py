class Solution:
    def trap(self, height: List[int]) -> int:
        
        total_water_area = 0
        left_max, right_max = 0, 0
        l, r = 0, len(height) - 1

        while l <= r:
            if left_max < right_max:
                water_area = max(left_max - height[l], 0)
                left_max = max(left_max, height[l])
                l += 1
            else:
                water_area = max(right_max - height[r], 0)
                right_max = max(right_max, height[r])
                r -= 1
            total_water_area += water_area

        return total_water_area
            


