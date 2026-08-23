from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def min_amount_needed(amount, coin_idx, coin_used):
            if coin_idx >= len(coins):
                if amount == 0:
                    return coin_used
                return 10001
            take = 10001
            if coins[coin_idx] <= amount:
                take = min_amount_needed(amount - coins[coin_idx], coin_idx, coin_used + 1)
            leave = min_amount_needed(amount, coin_idx + 1, coin_used)
            return min(take, leave)
        min_used = min_amount_needed(amount, 0, 0)
        if min_used == 10001:
            return -1
        return min_used