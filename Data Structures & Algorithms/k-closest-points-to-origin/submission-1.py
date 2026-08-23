from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_fn = lambda x: sqrt(x[0] ** 2 + x[1] ** 2)
        distances = list(enumerate(map(distance_fn, points)))
        distances = [(v, i) for i, v in distances]
        print(distances)
        heapq.heapify(distances)
        print(distances)
        indices = []
        for _ in range(k):
            value, index = heapq.heappop(distances)
            indices.append(index)

        output = []
        for i in indices:
            output.append(points[i])

        return output
            