import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        min_rate = math.ceil(total / h) # 16 
        max_rate = max(piles) # 25

        time = 0

        # binary search over the min_rate and max_rate to find the optimal time 
        while min_rate < max_rate:
            mid_rate = min_rate + (max_rate - min_rate) // 2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid_rate)
            if total_hours > h: # too slow; increase rate
                min_rate = mid_rate + 1
            elif total_hours <= h:
                max_rate = mid_rate
        
        return min_rate



        

        