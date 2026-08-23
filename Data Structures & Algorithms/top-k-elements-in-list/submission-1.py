import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        l = [(k, v) for k, v in num_count.items()]
        heapq.heapify(l)
        output = heapq.nlargest(k, l, key=lambda x: x[1])
        return [i[0] for i in output]

