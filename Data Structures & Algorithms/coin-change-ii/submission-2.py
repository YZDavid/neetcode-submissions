class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(2)]
        dp[0][0] = 1

        for coin in coins:
            dp[1] = dp[0]
            dp[0] = [0] * (amount + 1)
            dp[0][0] = 1
            for amt in range(amount + 1):
                remainder = amt - coin
                if remainder < 0:
                    ways = dp[1][amt]
                else:
                    ways = dp[0][remainder] + dp[1][amt]
                dp[0][amt] = ways
        return dp[0][-1]
            
        