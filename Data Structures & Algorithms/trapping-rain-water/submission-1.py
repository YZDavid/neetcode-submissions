class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = [0]
        postfix_max = [0]
        for h in height:
            prefix_max.append(max(prefix_max[-1], h))
        for h in height[::-1]:
            postfix_max.append(max(postfix_max[-1], h))
        sum_heights = 0
        for i, h in enumerate(height):
            left_max = prefix_max[i]
            right_max = postfix_max[len(height) - 1 - i]
            minimax = min(left_max, right_max)
            sum_heights += max(minimax - h, 0)
        print(prefix_max)
        print(postfix_max)
        return sum_heights

        