class Solution:
    def findMin(self, nums: List[int]) -> int:
        def condition(x):
            return nums[x] <= nums[-1]
        
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if condition(m):
                r = m
            else:
                l = m + 1
        return nums[l]
        