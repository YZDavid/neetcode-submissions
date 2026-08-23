class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, path):
            if index == len(nums):
                result.append(path[:])
                return
            
            # Skip choice
            backtrack(index + 1, path)

            # Choose choice
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()
        
        backtrack(0, [])
        return result
        