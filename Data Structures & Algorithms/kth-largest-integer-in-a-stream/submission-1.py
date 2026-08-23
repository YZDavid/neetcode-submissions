import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heap = nums.copy()
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        self.heap = heap

    def add(self, val: int) -> int:
        self.nums.append(val)
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val >= self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
        
