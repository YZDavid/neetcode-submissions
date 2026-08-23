class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        md_stack = []
        output = []
        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]
            if md_stack:
                while md_stack and temp >= md_stack[-1][0]:
                    md_stack.pop()
            if not md_stack:
                output.append(0)
            else:
                output.append(md_stack[-1][1] - i)
            md_stack.append((temp, i))
        return output[::-1]

