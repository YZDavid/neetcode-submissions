class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(index, choice):
            if index == len(nums):
                result.append(choice[:])
                return
            
            # Choose
            choice.append(nums[index])
            backtrack(index + 1, choice)
            choice.pop()

            # Do not choose
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtrack(index + 1, choice)
        
        backtrack(0, [])
        return result