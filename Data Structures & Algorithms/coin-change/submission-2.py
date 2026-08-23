class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def cc(amount):
            res = 1e9
            if amount < 0:
                return res
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            for coin in coins:
                res = min(res, 1 + cc(amount - coin))
            
            memo[amount] = res
            return res
        min_coins = cc(amount)
        return -1 if min_coins == 1e9 else min_coins