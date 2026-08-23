class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
        output = 1
        for i, num in enumerate(nums):
            max_lis = 0
            for j in range(0, i):
                if num > nums[j]:
                    max_lis = max(max_lis, lis[j])
            lis[i] = max_lis + 1
            output = max(output, max_lis + 1)
        return output