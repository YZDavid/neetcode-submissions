class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for num in nums:
            # If there exists a number exactly 1 smaller,
            # it is not the smallest in the sequence
            if num - 1 in set_nums:
                continue
            sequence = 1
            next_num = num + 1
            while next_num in set_nums:
                sequence += 1
                next_num += 1
            longest = max(longest, sequence)
        return longest
