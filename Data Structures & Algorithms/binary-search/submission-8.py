class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def condition(k):
            return nums[k] >= target
        
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if condition(m):
                r = m
            else:
                l = m + 1
        
        if nums[l] == target:
            return l
        return -1
        
        