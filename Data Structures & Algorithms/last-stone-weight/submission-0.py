class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = [-i for i in stones]
        heapq.heapify(stone_heap)
        while len(stone_heap) > 1:
            stone1 = -heapq.heappop(stone_heap)
            stone2 = -heapq.heappop(stone_heap)
            if stone1 > stone2:
                new_stone = stone1 - stone2
                heapq.heappush(stone_heap, -new_stone)
            
        if stone_heap:
            return -stone_heap[0]
        return 0