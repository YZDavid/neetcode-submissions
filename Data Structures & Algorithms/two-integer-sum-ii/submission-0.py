class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ptr = 0
        r_ptr = len(numbers) - 1
        while l_ptr < r_ptr:
            l_num = numbers[l_ptr]
            r_num = numbers[r_ptr]
            two_sum = l_num + r_num
            if two_sum == target:
                return [l_ptr + 1, r_ptr + 1]
            if two_sum > target:
                r_ptr -= 1
            else:
                l_ptr += 1