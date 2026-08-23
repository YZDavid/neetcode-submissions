class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        decr_stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures) -1, -1, -1):
            temp = temperatures[i]
            while decr_stack and temp >= decr_stack[-1][0]:
                decr_stack.pop()
            if not decr_stack:
                res[i] = 0
            else:
                next_idx = decr_stack[-1][1]
                res[i] = next_idx - i
            decr_stack.append((temp, i))

        return res
                
