class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        # if word1 becomes empty, insert remaining chars from word2
        for i in range(n1 - 1, -1, -1): 
            dp[i][n2] = n1 - i
        
        # if word2 becomes empty, insert remaining chars from word1
        for i in range(n2 - 1, -1, -1):
            dp[n1][i] = n2 - i
        
        print(dp)

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                # if equal, no operations required, move back by 1 on both strings
                if word1[i] == word2[j]:
                    dp[i][j] = 0 + dp[i+1][j+1]
                else: # an operation is required
                    delete = dp[i+1][j]
                    insert = dp[i][j+1]
                    replace = dp[i+1][j+1]
                    dp[i][j] = 1 + min(insert, delete, replace)
        
        return dp[0][0]

        
        



        