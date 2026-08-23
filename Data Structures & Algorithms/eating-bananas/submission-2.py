import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest_pile = max(piles)
        def hours_given_speed(piles, speed):
            return sum(map(lambda x: math.ceil(x/speed), piles))

        l, r = 1, largest_pile
        while l <= r:
            speed = l + (r - l) // 2
            hours = hours_given_speed(piles, speed)
            print(speed, hours, l, r)
            if hours > h:
                # Took too long, speed should be increased
                if l == r:
                    return speed + 1
                l = speed + 1
            elif hours < h:
                # Managed to eat within time limit, see if you can reduce speed
                if l == r:
                    return speed
                r = speed - 1
            elif l != r:
                # Found optimal? See if you can keep reducing speed
                r = speed - 1
            else:
                # Truly found the precise speed
                return speed
        return speed