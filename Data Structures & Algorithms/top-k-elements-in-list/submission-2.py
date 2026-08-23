import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        bucket = [[] for i in range(len(nums) + 1)]
        for num, count in num_count.items():
            bucket[count].append(num)
        output = []
        for i in range(len(nums), 0, -1):
            for j in bucket[i]:
                if k == 0:
                    return output
                output.append(j)
                k -= 1
        return output

