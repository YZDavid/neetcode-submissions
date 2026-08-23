class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def generator(nums, gen_list):
            if not nums:
                output.append(gen_list.copy())
                return

            # Include number
            gen_list.append(nums[0])
            generator(nums[1:], gen_list)

            # Do not include number
            gen_list.pop()
            generator(nums[1:], gen_list)
        
        generator(nums, [])
        return output

            
            