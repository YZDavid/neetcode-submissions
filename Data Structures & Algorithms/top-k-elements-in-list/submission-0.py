class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        sorted_nums = sorted([(k, v) for k, v in num_count.items()], key=lambda x: x[1], reverse=True)
        return [i[0] for i in sorted_nums[:k]]