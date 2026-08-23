class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, remainder, choice):
            if remainder == 0:
                result.append(choice[:])
                return
            if remainder < 0:
                return
            if index == len(nums):
                return
            # Choose
            choice.append(nums[index])
            backtrack(index, remainder - nums[index], choice)
            choice.pop()

            # Do not choose
            backtrack(index + 1, remainder, choice)
        
        backtrack(0, target, [])
        return result