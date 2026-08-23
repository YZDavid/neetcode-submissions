class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        def generate(index, generated_lst):
            if index == len(nums):
                output.append(generated_lst.copy())
                return
            
            # Choose value
            generated_lst.append(nums[index])
            generate(index + 1, generated_lst)

            # Do not choose value
            generated_lst.pop()
            next_idx = index + 1
            while next_idx < len(nums):
                if nums[index] != nums[next_idx]:
                    break
                index = next_idx
                next_idx += 1
            generate(index + 1, generated_lst)

        generate(0, [])
        return output