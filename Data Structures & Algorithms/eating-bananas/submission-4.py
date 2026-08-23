import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_complete(k):
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile / k)
            return time_taken <= h
        
        l, r = 1, max(piles)
        while l < r:
            m = l + (r - l) // 2
            if can_complete(m):
                r = m
            else:
                l = m + 1
        return l