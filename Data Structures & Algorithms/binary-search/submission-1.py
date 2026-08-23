class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = len(nums) // 2
        middle_num = nums[idx]
        if middle_num == target:
            return idx
        if len(nums) <= 1:
            return -1
        if middle_num < target:
            recursive_res = self.search(nums[idx:], target)
            if recursive_res == -1:
                return -1
            return idx + recursive_res
        if middle_num > target:
            return self.search(nums[:idx], target)