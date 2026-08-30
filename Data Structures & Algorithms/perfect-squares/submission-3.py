class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # Make list of valid squares for 'n'
        squares = []
        for x in range(1, (int(math.sqrt(n)) + 1)):
            squares.append(x*x)
        
        # squares = [1,4,9]

        for i in range(1, n + 1):
            for square in squares:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        
        return dp[n]

        
            



        

        