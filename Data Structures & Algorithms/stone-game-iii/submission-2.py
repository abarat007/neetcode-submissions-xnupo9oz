class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        alice_score = 0
        bob_score = 0
        n = len(stoneValue)
        dp = [0] * (n+3)

        # dp[idx] store the current player's best possible score advantage starting at this idx
        for idx in range(n-1, -1, -1):
            curr_taken = 0 
            best = float('-inf')

            # a player can take 1,2, or 3 stones at a time
            for take in range(1, 4):
                if idx + take - 1 >= n:
                    break
                curr_taken += stoneValue[idx + take - 1]
                best = max(best, curr_taken - dp[idx + take])
            
            dp[idx] = best
        
        # print(dp)
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
                



        
   



        
        




        