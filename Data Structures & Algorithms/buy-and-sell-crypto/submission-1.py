class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        suffix_max = prices.copy()
        for i in range(len(prices)-2, -1, -1):
            suffix_max[i] = max(suffix_max[i], suffix_max[i+1])
        
        best_price = 0
        for i in range(len(prices) - 1):
            buy_price = prices[i]
            best_sell_price = suffix_max[i+1]
            profit = best_sell_price - buy_price
            best_price = max(best_price, profit)
        
        return best_price