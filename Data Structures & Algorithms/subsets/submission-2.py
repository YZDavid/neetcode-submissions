class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        curr = []
        def backtrack(idx, curr):
            if idx == len(nums):
                output.append(curr[:])
                return
            # Choose
            curr.append(nums[idx])
            backtrack(idx + 1, curr)
            curr.pop()
            # Do not choose
            backtrack(idx + 1, curr)
        
        backtrack(0, curr)
        return output

        