class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            curr_num = nums[i]
            tmp = max_prod
            max_prod = max(curr_num, curr_num * min_prod, curr_num * max_prod)
            min_prod = min(curr_num, curr_num * min_prod, curr_num * tmp)
            res = max(res, max_prod)
        
        return res
