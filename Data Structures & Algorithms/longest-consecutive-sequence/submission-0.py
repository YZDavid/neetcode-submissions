class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_set = set(nums)
        longest = 0
        for num in number_set:
            curr_longest = 1
            if num - 1 in number_set:
                continue
            n = num
            while n + 1 in number_set:
                n += 1
                curr_longest += 1
            longest = max(longest, curr_longest)

        return longest