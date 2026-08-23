class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        max_profit = 0
        while right < len(prices):
            lowest_price = prices[left]
            curr_price = prices[right]
            profit = curr_price - lowest_price
            if profit < 0:
                # Because we found the new lowest
                left = right
            else:
                max_profit = max(max_profit, profit)
            right += 1
        return max_profit
        