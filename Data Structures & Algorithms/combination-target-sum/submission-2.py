class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def backtrack(idx, remainder, curr):
            if idx == len(nums):
                return
            if remainder < 0:
                return
            if remainder == 0:
                output.append(curr[:])
                return
            # Choose
            curr.append(nums[idx])
            backtrack(idx, remainder - nums[idx], curr)
            curr.pop()
            # Do not choose
            backtrack(idx + 1, remainder, curr)
        backtrack(0, target, [])
        return output