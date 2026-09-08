class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        rows = amount + 1
        cols = len(coins) + 1
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        # dp[r][c] represents how many ways I can make r (amt) based on the first 'c' coins in the coins list 

        # dp[1][1] should be 1, b/c only coin value 1 can make amount value 1

        # rows = amounts
        # cols = first 'c' coins from coins list
        for r in range(rows):
            for c in range(cols):
                if r == 0:
                    dp[r][c] = 1
                elif c == 0:
                    dp[r][c] = 0
                else:
                    coin = coins[c-1]
                    # Option 1: use the coin
                    with_coin = 0
                    diff = r - coin
                    if diff >= 0:
                        with_coin = dp[diff][c]
                    # Option 2: don't use the coin
                    without_coin = dp[r][c-1]

                    dp[r][c] = with_coin + without_coin
        
        return dp[amount][len(coins)]



                        

