class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        presum = [1]
        postsum = [1]
        for i in nums:
            presum.append(presum[-1] * i)
        for i in nums[::-1]:
            postsum.append(postsum[-1] * i)
        postsum = postsum[::-1]
        output = []
        for i in range(len(nums)):
            output.append(postsum[i+1] * presum[i])
        print(presum)
        print(postsum)
        return output
