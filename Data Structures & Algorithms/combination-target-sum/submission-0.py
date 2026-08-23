class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort(reverse=True)
        output = []
        def generator(index, target, generated_lst):
            if target == 0:
                output.append(generated_lst.copy())
                return
            if target < 0:
                return
            if index == len(nums):
                return

            # Pick the first number, then continue picking the first number
            chosen_num = nums[index]
            remaining = target - chosen_num
            generated_lst.append(chosen_num)
            generator(index, remaining, generated_lst)

            # Skip this number, then move on to pick the next number
            generated_lst.pop()
            generator(index + 1, target, generated_lst)

        generator(0, target, [])
        return output
