class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def generator(nums, generated_lst):
            if not nums:
                output.append(generated_lst.copy())
                return
            
            for i in range(len(nums)):
                remaining_lst = nums.copy()
                chosen = remaining_lst.pop(i)
                generated_lst.append(chosen)
                generator(remaining_lst, generated_lst)
                generated_lst.pop()
            
        generator(nums, [])
        return output



            