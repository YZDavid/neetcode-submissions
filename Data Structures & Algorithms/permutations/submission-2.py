class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursive(idx):
            if idx == len(nums):
                return [[]]
            output_arr = []
            input_arr = recursive(idx + 1)
            for arr in input_arr:
                for i in range(len(nums)-idx):
                    copy_arr = arr[:]
                    copy_arr.insert(i, nums[idx])
                    output_arr.append(copy_arr)
            return output_arr
        return recursive(0)

