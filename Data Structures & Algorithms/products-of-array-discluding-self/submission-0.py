class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # trivial case
        if len(nums) == 2:
            return [nums[1], nums[0]]
        
        # non trivial where length greater than 3
        left_cum = [1] * len(nums)
        right_cum = [1] * len(nums)
        left_cum[0] = nums[0]
        right_cum[-1] = nums[-1]

        for i in range(1, len(nums)):
            left_idx = i
            right_idx = len(nums) -1 - i
            left_cum[left_idx] *= nums[left_idx] * left_cum[left_idx - 1]
            right_cum[right_idx] *= nums[right_idx] * right_cum[right_idx + 1]
        
        output = []
        for i in range(len(nums)):
            l = i - 1
            r = i + 1
            left = left_cum[l]
            if l < 0:
                left = 1
            if r > len(nums) - 1:
                right = 1
            else:
                right = right_cum[r]
            output.append(left * right)
        return output
            
            

        