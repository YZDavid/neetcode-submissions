class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashset = set()
        for num in nums:
            hashset.add(num)
        longest = 1
        for num in nums:
            if num - 1 in hashset:
                continue
            sequence = 0
            while num in hashset:
                sequence += 1
                num += 1
            longest = max(longest, sequence)
        return longest