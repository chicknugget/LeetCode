class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        ways = [0] * (amount + 1)
        ways[0] = 1
        
        for coin in coins:
            for i in range(coin, amount + 1):
                ways[i] += ways[i - coin]
                
        return ways[amount]