class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        output = set()

        def generate(nums, generated_lst):
            if not nums:
                output.add(tuple(generated_lst))
                return
            
            # Add value to generated list
            generated_lst.append(nums[0])
            generate(nums[1:], generated_lst)

            # Do not add value to generated list
            generated_lst.pop()
            generate(nums[1:], generated_lst)

        generate(sorted_nums, [])
        return [list(i) for i in output]