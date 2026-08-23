class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = list(zip(position, speed))
        position_speed.sort(key=lambda x: x[0])
        time_taken = [((target - pos) / speed) for pos, speed in position_speed]
        stack = []
        for i in range(len(time_taken)-1, -1, -1):
            time = time_taken[i]
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
        
        return len(stack)