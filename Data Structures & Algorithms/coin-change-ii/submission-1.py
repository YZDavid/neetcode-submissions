from functools import cache
import sys

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        sys.setrecursionlimit(2000)
        @cache
        def count_change(amount, coin_idx):
            if coin_idx == len(coins):
                return 1 if amount == 0 else 0
            take = 0
            if coins[coin_idx] <= amount:
                take = count_change(amount - coins[coin_idx], coin_idx)
            leave = count_change(amount, coin_idx + 1)
            return take + leave
        return count_change(amount, 0)