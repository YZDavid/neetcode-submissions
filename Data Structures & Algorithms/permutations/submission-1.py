class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        output = []
        prev_permute = self.permute(nums[1:])
        for permute in prev_permute:
            for i in range(len(permute)+1):
                permute_copy = permute.copy()
                permute_copy.insert(i, nums[0])
                output.append(permute_copy)
        return output

