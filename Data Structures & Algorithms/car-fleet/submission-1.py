class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for s, p in zip(speed, position)]
        cars.sort(key=lambda x:x[0], reverse=True)
        stack = []
        for p, s in cars:
            time_taken = (target - p) / s
            stack.append(time_taken)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        print(cars)
        return len(stack)