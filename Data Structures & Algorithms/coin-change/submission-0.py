class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0
        for current_amount in range(amount + 1):
            for coin in coins:
                if current_amount - coin >= 0:
                    dp[current_amount]= min(dp[current_amount], 1 + dp[current_amount - coin])
        if dp[amount] == float("inf"):
            return -1
        else: return dp[amount]