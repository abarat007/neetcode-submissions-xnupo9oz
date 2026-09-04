class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        max_eating_rate = max(piles) # 4 bananas/hr

        low_eating_rate = 1
        high_eating_rate = max_eating_rate # 4

        while low_eating_rate < high_eating_rate:
            mid_eating_rate = low_eating_rate + (high_eating_rate - low_eating_rate) // 2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/mid_eating_rate)
            if total_hours > h:
                low_eating_rate = mid_eating_rate + 1
            elif total_hours <= h:
                high_eating_rate = mid_eating_rate
        
        return low_eating_rate



        